import datetime as dt
import hashlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from .meta import datasets


@dataclass
class File:
    filepath: Path
    dataset: str
    partition: str
    date: dt.date
    extension: str
    size: int
    # checksum: str = None
    is_most_recent: bool = False


@dataclass
class RemoteFile:
    filename: str
    full_path: str
    datetime: dt.datetime
    extension: str
    size: int
    dataset: str = None
    partition: dict = field(default_factory=dict)


def get_sha1_hash(filepath: Path | str) -> str:
    """Returns the SHA1 hash of a file."""
    sha1 = hashlib.sha1()
    with open(filepath, "rb") as f:
        while True:
            data = f.read(65_536)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()


def get_filename(remote_file: RemoteFile) -> str:
    """Returns the filename for the given file info and partition."""
    dataset = remote_file.dataset
    extension = remote_file.extension
    file_datetime = remote_file.datetime.strftime("%Y%m%d")
    metadata_partition = datasets[dataset]["partition"]
    match metadata_partition:
        case ["uf"]:
            uf = remote_file.partition["uf"].lower()
            partition = f"{uf}"
        case ["year"]:
            year = remote_file.partition["year"]
            partition = f"{year}"
        case ["uf", "year"]:
            uf = remote_file.partition["uf"].lower()
            year = remote_file.partition["year"]
            partition = f"{year}-{uf}"
        case ["uf", "yearmonth"]:
            uf = remote_file.partition["uf"].lower()
            year = remote_file.partition["year"]
            month = remote_file.partition["month"]
            partition = f"{year}{month:02}-{uf}"
        case _:
            partition = ""
    if version := remote_file.partition.get("version"):
        partition += f"-{version}"
    filename = "_".join([s for s in (dataset, partition, file_datetime) if s])
    return f"{filename}.{extension}"


def get_file_metadata(file: Path) -> File:
    """Returns a dict with the parsed filename."""
    dataset, partition, file_date = file.stem.split("_")
    extension = file.suffix
    file_date = dt.datetime.strptime(file_date, "%Y%m%d").date()
    size = file.stat().st_size
    return File(
        filepath=file,
        size=size,
        dataset=dataset,
        partition=partition,
        date=file_date,
        # checksum=get_sha1_hash(file),
        extension=extension,
    )


def get_files_metadata(dirpath: Path, extension: str) -> File:
    files = {}
    for f in dirpath.glob(f"*.{extension}"):
        file = get_file_metadata(f)
        if file.partition not in files:
            files[file.partition] = []
        files[file.partition].append(file)
    for partition in files:
        partition_files_sorted = sorted(
            files[partition],
            key=lambda f: f.filepath.name,
        )
        n_files_partition_sorted = len(partition_files_sorted)
        for i, file in enumerate(partition_files_sorted, 1):
            file.is_most_recent = i == n_files_partition_sorted
            yield file


def get_most_recent(files: Iterable[File]) -> dict[str, File]:
    most_recent_files = [file for file in files if file.is_most_recent]
    return most_recent_files
