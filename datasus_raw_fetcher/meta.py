# Brazil UFs
states = [
    "AC",
    "AL",
    "AP",
    "AM",
    "BA",
    "CE",
    "DF",
    "ES",
    "GO",
    "MA",
    "MT",
    "MS",
    "MG",
    "PA",
    "PB",
    "PR",
    "PE",
    "PI",
    "RJ",
    "RN",
    "RS",
    "RO",
    "RR",
    "SC",
    "SP",
    "SE",
    "TO",
    "BR",
]

uf_pattern = "{}".format("|".join(states).lower())
month_pattern = "|".join((f"{i:02}" for i in range(1, 12 + 1)))
year_4digit_pattern = r"\d{4}"  # 1997
year_2digit_pattern = r"\d{2}"  # 97

# 9701, 9702, ... 9712, 9801, ...
year_pattern = r"({yearly})".format(
    yearly=year_4digit_pattern,
)
year2_pattern = r"({yearly})".format(
    yearly=year_2digit_pattern,
)
uf_year_pattern = r"({uf})({yearly})".format(
    uf=uf_pattern,
    yearly=year_4digit_pattern,
)
uf_year2_pattern = r"({uf})({yearly})".format(
    uf=uf_pattern,
    yearly=year_2digit_pattern,
)
uf_year2_month_pattern = r"({uf})({year})({month})".format(
    uf=uf_pattern,
    year=year_2digit_pattern,
    month=month_pattern,
)

BASE_PATH = "/dissemin/publicos"

datasets = {
    "sih-rd": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIHSUS/199201_200712/Dados",
                "filename_prefix": "RD",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SIHSUS/200801_/Dados",
                "filename_prefix": "RD",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sih-rj": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIHSUS/200801_/Dados",
                "filename_prefix": "RJ",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sih-sp": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIHSUS/199201_200712/Dados",
                "filename_prefix": "SP",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SIHSUS/200801_/Dados",
                "filename_prefix": "SP",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sih-er": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIHSUS/200801_/Dados",
                "filename_prefix": "ER",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sinasc": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINASC/1994_1995/Dados/DNRES",
                "filename_prefix": "DNR",
                "filename_pattern": uf_year_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SINASC/1996_/Dados/DNRES",
                "filename_prefix": "DN",
                "filename_pattern": uf_year_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinasc-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINASC/PRELIM/DNRES",
                "filename_prefix": "DN",
                "filename_pattern": uf_year_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sim-do-cid09": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID9/DORES",
                "filename_prefix": "DOR",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sim-do-cid10": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID10/DORES",
                "filename_prefix": "DO",
                "filename_pattern": uf_year_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sim-do-cid10-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/PRELIM/DORES",
                "filename_prefix": "DO",
                "filename_pattern": uf_year_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sim-doext-cid09": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID9/DOFET",
                "filename_prefix": "DOEXT",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "year",
    },
    "sim-doext-cid10": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID10/DOFET",
                "filename_prefix": "DOEXT",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "year",
    },
    "sim-doext-cid10-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/PRELIM/DOFET",
                "filename_prefix": "DOEXT",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "year",
    },
    "sim-dofet-cid09": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID9/DOFET",
                "filename_prefix": "DOFET",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "year",
    },
    "sim-dofet-cid10": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID10/DOFET",
                "filename_prefix": "DOFET",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "year",
    },
    "sim-dofet-cid10-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/PRELIM/DOFET",
                "filename_prefix": "DOFET",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "year",
    },
    "sim-doinf-cid09": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID9/DOFET",
                "filename_prefix": "DOINF",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "year",
    },
    "sim-doinf-cid10": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID10/DOFET",
                "filename_prefix": "DOINF",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "year",
    },
    "sim-doinf-cid10-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/PRELIM/DOFET",
                "filename_prefix": "DOINF",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "year",
    },
    "sim-domat-cid10": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/CID10/DOFET",
                "filename_prefix": "DOMAT",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "year",
    },
    "sim-domat-cid10-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIM/PRELIM/DOFET",
                "filename_prefix": "DOMAT",
                "filename_pattern": year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "year",
    },
    "cnes-dc": {
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/DC",
                "filename_prefix": "DC",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "cnes-ee": {
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/EE",
                "filename_prefix": "EE",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "cnes-ef": {
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/EF",
                "filename_prefix": "EF",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "cnes-ep": {
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/EP",
                "filename_prefix": "EP",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "cnes-eq": {
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/EQ",
                "filename_prefix": "EQ",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "cnes-gm": {
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/GM",
                "filename_prefix": "GM",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "cnes-hb": {
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/HB",
                "filename_prefix": "HB",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "cnes-in": {
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/IN",
                "filename_prefix": "IN",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "cnes-lt": {
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/LT",
                "filename_prefix": "LT",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "cnes-pf": {
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/PF",
                "filename_prefix": "PF",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "cnes-rc": {
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/RC",
                "filename_prefix": "RC",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "cnes-sr": {
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/SR",
                "filename_prefix": "SR",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "cnes-st": {
        "periods": [
            {
                "dir": BASE_PATH + "/CNES/200508_/Dados/ST",
                "filename_prefix": "ST",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sia-ab": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "AB",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sia-abo": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "ABO",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sia-acf": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "ACF",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sia-ad": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "AD",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sia-am": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "AM",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sia-an": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "AN",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sia-aq": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "AQ",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sia-ar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "AR",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sia-atd": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "ATD",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sia-pa": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/199407_200712/Dados",
                "filename_prefix": "PA",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "PA",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sia-ps": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "PS",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sia-sad": {
        "periods": [
            {
                "dir": BASE_PATH + "/SIASUS/200801_/Dados",
                "filename_prefix": "SAD",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "cih-cr": {
        "periods": [
            {
                "dir": BASE_PATH + "/CIH/200801_201012/Dados",
                "filename_prefix": "CR",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "ciha": {
        "periods": [
            {
                "dir": BASE_PATH + "/CIHA/201101_/Dados",
                "filename_prefix": "CIHA",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "resp": {
        "periods": [
            {
                "dir": BASE_PATH + "/RESP/DADOS",
                "filename_prefix": "RESP",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sisprenatal-pn": {
        "periods": [
            {
                "dir": BASE_PATH + "/SISPRENATAL/201201_/Dados",
                "filename_prefix": "PN",
                "filename_pattern": uf_year2_month_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-yearmonth",
    },
    "sinan-acbi": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "ACBI",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-acbi-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "ACBI",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-acgr": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "ACGR",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-acgr-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "ACGR",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-anim": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "ANIM",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-anim-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "ANIM",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-antr": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "ANTR",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-antr-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "ANTR",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-botu": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "BOTU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-botu-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "BOTU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-canc": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "CANC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-canc-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "CANC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-chag": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "CHAG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-chag-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "CHAG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-chik": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "CHIK",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-chik-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "CHIK",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-cole": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "COLE",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-cole-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "COLE",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-coqu": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "COQU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-coqu-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "COQU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-deng": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "DENG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-deng-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "DENG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-derm": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "DERM",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-derm-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "DERM",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-dift": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "DIFT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-dift-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "DIFT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-esqu": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "ESQU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-esqu-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "ESQU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-fama": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "FAMA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-fama-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "FAMA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-fmac": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "FMAC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-fmac-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "FMAC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-ftif": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "FTIF",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-ftif-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "FTIF",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-hans": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "HANS",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-hans-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "HANS",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-hant": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "HANT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-hant-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "HANT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-hepa": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "HEPA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-hepa-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "HEPA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-iexo": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "IEXO",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-iexo-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "IEXO",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-iexo": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "IEXO",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-iexo-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "IEXO",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-infl": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "INFL",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-infl-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "INFL",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-leiv": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "LEIV",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-leiv-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "LEIV",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-lept": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "LEPT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-lept-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "LEPT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-lerd": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "LERD",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-lerd-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "LERD",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-ltan": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "LTAN",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-ltan-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "LTAN",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-mala": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "MALA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-mala-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "MALA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-meni": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "MENI",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-meni-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "MENI",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-ment": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "MENT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-ment-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "MENT",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-pair": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "PAIR",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-pair-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "PAIR",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-pest": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "PEST",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-pest-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "PEST",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-pfan": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "PFAN",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-pfan-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "PFAN",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-pneu": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "PNEU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-pneu-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "PNEU",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-raiv": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "RAIV",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-raiv-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "RAIV",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-sifa": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "SIFA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-sifa-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "SIFA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-sifc": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "SIFC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-sifc-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "SIFC",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-sifg": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "SIFG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-sifg-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "SIFG",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-teta": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "TETA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-teta-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "TETA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-tetn": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "TETN",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-tetn-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "TETN",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-tube": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "TUBE",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-tube-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "TUBE",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-viol": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "VIOL",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-viol-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "VIOL",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-zika": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/FINAIS",
                "filename_prefix": "ZIKA",
                "filename_pattern": uf_year2_pattern,
                "extension": "dbc",
            },
        ],
        "partition": "uf-year",
    },
    "sinan-zika-preliminar": {
        "periods": [
            {
                "dir": BASE_PATH + "/SINAN/DADOS/PRELIM",
                "filename_prefix": "ZIKA",
                "filename_pattern": uf_year2_pattern,
            },
        ],
        "partition": "uf-year",
    },
}
