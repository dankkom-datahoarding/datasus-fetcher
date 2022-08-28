import datetime as dt
import ftplib
import queue
import re
import threading
import time
from functools import lru_cache
from pathlib import Path

from . import meta
from .storage import RemoteFile, get_filename, get_sha1_hash

FTP_HOST = "ftp.datasus.gov.br"
MEGA = 1_000_000


class Fetcher(threading.Thread):

    def __init__(self, q: queue.Queue, dest_dir: Path):
        super().__init__()
        self.daemon = True
        self.ftp = connect()
        self.q = q
        self.dest_dir = dest_dir

    def run(self):
        while True:
            file: RemoteFile = self.q.get()
            dataset = file.dataset
            filename = get_filename(file)

            partition_dir = ""
            if "year" in file.partition:
                partition_dir += f"{file.partition['year']}"
            if "month" in file.partition:
                partition_dir += f"{file.partition['month']:02d}"

            filepath: Path = self.dest_dir / dataset / partition_dir / filename
            if filepath.exists() and filepath.stat().st_size == file.size:
                self.q.task_done()
                continue
            filepath.parent.mkdir(parents=True, exist_ok=True)

            try:
                print(file.full_path, "->", filepath)
                t0 = time.time()
                sha1 = fetch_file(self.ftp, file.full_path, filepath)
                tt = time.time() - t0
                log_download(tt, file.size, sha1)
            except Exception as e:
                print(f"Exception {e}")
            finally:
                self.q.task_done()


def log_download(tt: float, size: int, sha1=""):
    filesize_mb = size / MEGA
    download_speed_mbps = (size * 8) / tt / MEGA
    log = " ".join(
        [
            f"{sha1: >46}",
            f"{filesize_mb: >6.2f} MB",
            f"{tt: >5.2f} s",
            f"{download_speed_mbps: >5.2f} Mb/s",
        ]
    )
    print(log)


def connect() -> ftplib.FTP:
    """Connects to the FTP server."""
    ftp = ftplib.FTP(FTP_HOST, encoding="latin-1")
    ftp.login()
    return ftp


@lru_cache
def list_files(ftp: ftplib.FTP, directory: str, retries: int = 3) -> list[dict]:
    try:
        ftp.cwd(directory)
    except ftplib.error_perm:
        print(f"Directory not found. {directory}")

    while retries > 0:
        files = []
        try:
            ftp.retrlines("LIST", files.append)
            break
        # Timeout exception
        except (ftplib.error_temp, TimeoutError):
            print(f"Timeout exception while listing files.")
            retries -= 1
            time.sleep(5)

    # parse files' date, size and name
    def parse_line(line):
        date, time, size, name = line.split()
        extension = name.rsplit(".", maxsplit=1)[1].lower()
        datetime = dt.datetime.strptime(date + " " + time, "%m-%d-%y %I:%M%p")
        try:
            size = int(size)
        except ValueError:
            size = None
        return {
            "datetime": datetime,
            "size": size,
            "filename": name,
            "extension": extension,
            "full_path": f"{directory}/{name}",
        }

    files = [parse_line(line) for line in files]

    return files


def fetch_file(
    ftp: ftplib.FTP,
    path: str,
    dest_filepath: Path | str,
    retries: int = 3,
) -> str:
    """Fetch a file from a remote FTP server.

    :param path: The path to the file.
    :param dest_filepath: The destination file path.
    :param ftp: The FTP connection.
    """

    if isinstance(dest_filepath, str):
        dest_filepath = Path(dest_filepath.lower())
    if not dest_filepath.parent.exists():
        dest_filepath.parent.mkdir(parents=True)

    while retries > 0:
        try:
            with open(dest_filepath, "wb") as f:
                ftp.retrbinary("RETR " + path, f.write)
            sha1 = get_sha1_hash(dest_filepath)
            return sha1
        # File not found exception
        except ftplib.error_perm:
            print(f"File {path} not found.")
            dest_filepath.unlink(missing_ok=True)
            return
        # Timeout exception
        except (ftplib.error_temp, TimeoutError):
            print(f"Timeout exception for {path}.")
            dest_filepath.unlink(missing_ok=True)
            retries -= 1
            time.sleep(5)


def get_year2(year_: str) -> int:
    if year_[0] in "789":
        year = 1900 + int(year_)
    else:
        year = 2000 + int(year_)
    return year


def parse_uf_year2_month_filename(m: re.Match) -> dict:
    uf = m.group(1)
    year_ = m.group(2)
    year = get_year2(year_)
    month = int(m.group(3))
    return {
        "uf": uf,
        "year": year,
        "month": month,
    }


def parse_year_filename(m: re.Match) -> dict:
    year = int(m.group(1))
    return {
        "year": year,
    }


def parse_year2_filename(m: re.Match) -> dict:
    year_ = m.group(1)
    year = get_year2(year_)
    return {
        "year": year,
    }


def parse_uf_year_filename(m: re.Match) -> dict:
    uf = m.group(1)
    year = int(m.group(2))
    return {
        "uf": uf,
        "year": year,
    }


def parse_uf_year2_filename(m: re.Match) -> dict:
    uf = m.group(1)
    year_ = m.group(2)
    year = get_year2(year_)
    return {
        "uf": uf,
        "year": year,
    }


def parse_uf_filename(m: re.Match) -> dict:
    uf = m.group(1)
    return {
        "uf": uf,
    }


def parse_uf_year2_month_filename_sia_pa(m: re.Match) -> dict:
    uf = m.group(1)
    year_ = m.group(2)
    year = get_year2(year_)
    month = int(m.group(3))
    version = m.group(4)
    return {
        "uf": uf,
        "year": year,
        "month": month,
        "version": version,
    }


def parse_filename(m: re.Match, pattern: str) -> dict:
    match pattern:
        case meta.uf_year_pattern:
            return parse_uf_year_filename(m)
        case meta.uf_year2_pattern:
            return parse_uf_year2_filename(m)
        case meta.uf_year2_month_pattern:
            return parse_uf_year2_month_filename(m)
        case meta.uf_year2_month_pattern_sia_pa:
            return parse_uf_year2_month_filename_sia_pa(m)
        case meta.year_pattern:
            return parse_year_filename(m)
        case meta.year2_pattern:
            return parse_year2_filename(m)
        case meta.uf_mapas_year_pattern:
            return parse_uf_year_filename(m)
        case meta.uf_cnv_pattern:
            return parse_uf_filename(m)
        case "base_territorial":
            return {}
        case _:
            raise ValueError(f"Pattern not found: {pattern}")


def list_dataset_files(ftp: ftplib.FTP, dataset: str) -> list[RemoteFile]:
    dataset_files = []
    for period in meta.datasets[dataset]["periods"]:
        files = [
            RemoteFile(**f)
            for f in list_files(ftp, directory=period["dir"], retries=3)
        ]
        fn_prefix = period["filename_prefix"]
        fn_pattern = period["filename_pattern"]
        fn_ext = period["extension"]
        pattern = re.compile(f"^{fn_prefix}{fn_pattern}\\.{fn_ext}$".lower())
        for file in files:
            m = pattern.match(file.filename.lower())
            if m:
                file.dataset = dataset
                file.partition |= parse_filename(m, fn_pattern)
                dataset_files.append(file)
    return dataset_files


def download_documentation(
    ftp: ftplib.FTP,
    dataset: str,
    destdir: Path,
):

    destdir = destdir / f"{dataset}[doc]"

    ftp_dir = meta.docs[dataset]["dir"]
    ftp.cwd(ftp_dir)

    files = list_files(ftp)

    for i, file in enumerate(files):
        filename, extension = file["filename"].rsplit(".", 1)
        filename = f"{filename}@{file['datetime']:%Y%m%d}.{extension}"
        filepath = destdir / filename
        print(f"{i: >5}", file["full_path"], "->", filepath)
        t0 = time.time()
        sha1 = fetch_file(ftp, file["full_path"], filepath)
        tt = time.time() - t0
        filesize_kb = f"{file['size'] / 1024:.2f} kB"
        download_speed_kbps = f"{file['size'] / tt / 1024:.2f} kB/s"
        print(f"      {sha1} {tt:.2f} s {filesize_kb} {download_speed_kbps}")
