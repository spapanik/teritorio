from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Generic, Iterator, TypeVar

T = TypeVar("T")

class Singleton(type):
    instance: type[Singleton] | None

    def __init__(
        cls, name: str, bases: tuple[type[Singleton], ...], dict_: dict[str, Any]
    ): ...
    def __call__(cls) -> type[Singleton]: ...

class DataListIterator(Generic[T]):
    values: Iterator[T]
    def __init__(self, data: dict[str, T]) -> None: ...
    def __iter__(self) -> DataListIterator[T]: ...
    def __next__(self) -> T: ...

class DataList(Generic[T]):
    _data_path: Path
    _object_class: type[T]
    _data: dict[str, T]

    def __init__(self) -> None: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __len__(self) -> int: ...
    def __getitem__(self, key: str) -> T: ...
    def __iter__(self) -> DataListIterator[T]: ...

@dataclass(frozen=True, order=True)
class Country:
    english_name: str
    french_name: str
    alpha_2_code: str
    alpha_3_code: str
    numeric_code: int

class Countries(DataList[Country], metaclass=Singleton):
    ABW: Country
    AFG: Country
    AGO: Country
    AIA: Country
    ALA: Country
    ALB: Country
    AND: Country
    ARE: Country
    ARG: Country
    ARM: Country
    ASM: Country
    ATA: Country
    ATF: Country
    ATG: Country
    AUS: Country
    AUT: Country
    AZE: Country
    BDI: Country
    BEL: Country
    BEN: Country
    BES: Country
    BFA: Country
    BGD: Country
    BGR: Country
    BHR: Country
    BHS: Country
    BIH: Country
    BLM: Country
    BLR: Country
    BLZ: Country
    BMU: Country
    BOL: Country
    BRA: Country
    BRB: Country
    BRN: Country
    BTN: Country
    BVT: Country
    BWA: Country
    CAF: Country
    CAN: Country
    CCK: Country
    CHE: Country
    CHL: Country
    CHN: Country
    CIV: Country
    CMR: Country
    COD: Country
    COG: Country
    COK: Country
    COL: Country
    COM: Country
    CPV: Country
    CRI: Country
    CUB: Country
    CUW: Country
    CXR: Country
    CYM: Country
    CYP: Country
    CZE: Country
    DEU: Country
    DJI: Country
    DMA: Country
    DNK: Country
    DOM: Country
    DZA: Country
    ECU: Country
    EGY: Country
    ERI: Country
    ESH: Country
    ESP: Country
    EST: Country
    ETH: Country
    FIN: Country
    FJI: Country
    FLK: Country
    FRA: Country
    FRO: Country
    FSM: Country
    GAB: Country
    GBR: Country
    GEO: Country
    GGY: Country
    GHA: Country
    GIB: Country
    GIN: Country
    GLP: Country
    GMB: Country
    GNB: Country
    GNQ: Country
    GRC: Country
    GRD: Country
    GRL: Country
    GTM: Country
    GUF: Country
    GUM: Country
    GUY: Country
    HKG: Country
    HMD: Country
    HND: Country
    HRV: Country
    HTI: Country
    HUN: Country
    IDN: Country
    IMN: Country
    IND: Country
    IOT: Country
    IRL: Country
    IRN: Country
    IRQ: Country
    ISL: Country
    ISR: Country
    ITA: Country
    JAM: Country
    JEY: Country
    JOR: Country
    JPN: Country
    KAZ: Country
    KEN: Country
    KGZ: Country
    KHM: Country
    KIR: Country
    KNA: Country
    KOR: Country
    KWT: Country
    LAO: Country
    LBN: Country
    LBR: Country
    LBY: Country
    LCA: Country
    LIE: Country
    LKA: Country
    LSO: Country
    LTU: Country
    LUX: Country
    LVA: Country
    MAC: Country
    MAF: Country
    MAR: Country
    MCO: Country
    MDA: Country
    MDG: Country
    MDV: Country
    MEX: Country
    MHL: Country
    MKD: Country
    MLI: Country
    MLT: Country
    MMR: Country
    MNE: Country
    MNG: Country
    MNP: Country
    MOZ: Country
    MRT: Country
    MSR: Country
    MTQ: Country
    MUS: Country
    MWI: Country
    MYS: Country
    MYT: Country
    NAM: Country
    NCL: Country
    NER: Country
    NFK: Country
    NGA: Country
    NIC: Country
    NIU: Country
    NLD: Country
    NOR: Country
    NPL: Country
    NRU: Country
    NZL: Country
    OMN: Country
    PAK: Country
    PAN: Country
    PCN: Country
    PER: Country
    PHL: Country
    PLW: Country
    PNG: Country
    POL: Country
    PRI: Country
    PRK: Country
    PRT: Country
    PRY: Country
    PSE: Country
    PYF: Country
    QAT: Country
    REU: Country
    ROU: Country
    RUS: Country
    RWA: Country
    SAU: Country
    SDN: Country
    SEN: Country
    SGP: Country
    SGS: Country
    SHN: Country
    SJM: Country
    SLB: Country
    SLE: Country
    SLV: Country
    SMR: Country
    SOM: Country
    SPM: Country
    SRB: Country
    SSD: Country
    STP: Country
    SUR: Country
    SVK: Country
    SVN: Country
    SWE: Country
    SWZ: Country
    SXM: Country
    SYC: Country
    SYR: Country
    TCA: Country
    TCD: Country
    TGO: Country
    THA: Country
    TJK: Country
    TKL: Country
    TKM: Country
    TLS: Country
    TON: Country
    TTO: Country
    TUN: Country
    TUR: Country
    TUV: Country
    TWN: Country
    TZA: Country
    UGA: Country
    UKR: Country
    UMI: Country
    URY: Country
    USA: Country
    UZB: Country
    VAT: Country
    VCT: Country
    VEN: Country
    VGB: Country
    VIR: Country
    VNM: Country
    VUT: Country
    WLF: Country
    WSM: Country
    YEM: Country
    ZAF: Country
    ZMB: Country
    ZWE: Country

@dataclass(frozen=True, order=True)
class Currency:
    code: str
    name: str
    entities: tuple[str, ...]
    numeric_code: int
    minor_units: int | None

class Currencies(DataList[Currency], metaclass=Singleton):
    AED: Currency
    AFN: Currency
    ALL: Currency
    AMD: Currency
    ANG: Currency
    AOA: Currency
    ARS: Currency
    AUD: Currency
    AWG: Currency
    AZN: Currency
    BAM: Currency
    BBD: Currency
    BDT: Currency
    BGN: Currency
    BHD: Currency
    BIF: Currency
    BMD: Currency
    BND: Currency
    BOB: Currency
    BOV: Currency
    BRL: Currency
    BSD: Currency
    BTN: Currency
    BWP: Currency
    BYN: Currency
    BZD: Currency
    CAD: Currency
    CDF: Currency
    CHE: Currency
    CHF: Currency
    CHW: Currency
    CLF: Currency
    CLP: Currency
    CNY: Currency
    COP: Currency
    COU: Currency
    CRC: Currency
    CUC: Currency
    CUP: Currency
    CVE: Currency
    CZK: Currency
    DJF: Currency
    DKK: Currency
    DOP: Currency
    DZD: Currency
    EGP: Currency
    ERN: Currency
    ETB: Currency
    EUR: Currency
    FJD: Currency
    FKP: Currency
    GBP: Currency
    GEL: Currency
    GHS: Currency
    GIP: Currency
    GMD: Currency
    GNF: Currency
    GTQ: Currency
    GYD: Currency
    HKD: Currency
    HNL: Currency
    HTG: Currency
    HUF: Currency
    IDR: Currency
    ILS: Currency
    INR: Currency
    IQD: Currency
    IRR: Currency
    ISK: Currency
    JMD: Currency
    JOD: Currency
    JPY: Currency
    KES: Currency
    KGS: Currency
    KHR: Currency
    KMF: Currency
    KPW: Currency
    KRW: Currency
    KWD: Currency
    KYD: Currency
    KZT: Currency
    LAK: Currency
    LBP: Currency
    LKR: Currency
    LRD: Currency
    LSL: Currency
    LYD: Currency
    MAD: Currency
    MDL: Currency
    MGA: Currency
    MKD: Currency
    MMK: Currency
    MNT: Currency
    MOP: Currency
    MRU: Currency
    MUR: Currency
    MVR: Currency
    MWK: Currency
    MXN: Currency
    MXV: Currency
    MYR: Currency
    MZN: Currency
    NAD: Currency
    NGN: Currency
    NIO: Currency
    NOK: Currency
    NPR: Currency
    NZD: Currency
    OMR: Currency
    PAB: Currency
    PEN: Currency
    PGK: Currency
    PHP: Currency
    PKR: Currency
    PLN: Currency
    PYG: Currency
    QAR: Currency
    RON: Currency
    RSD: Currency
    RUB: Currency
    RWF: Currency
    SAR: Currency
    SBD: Currency
    SCR: Currency
    SDG: Currency
    SEK: Currency
    SGD: Currency
    SHP: Currency
    SLE: Currency
    SLL: Currency
    SOS: Currency
    SRD: Currency
    SSP: Currency
    STN: Currency
    SVC: Currency
    SYP: Currency
    SZL: Currency
    THB: Currency
    TJS: Currency
    TMT: Currency
    TND: Currency
    TOP: Currency
    TRY: Currency
    TTD: Currency
    TWD: Currency
    TZS: Currency
    UAH: Currency
    UGX: Currency
    USD: Currency
    USN: Currency
    UYI: Currency
    UYU: Currency
    UYW: Currency
    UZS: Currency
    VED: Currency
    VES: Currency
    VND: Currency
    VUV: Currency
    WST: Currency
    XAF: Currency
    XAG: Currency
    XAU: Currency
    XBA: Currency
    XBB: Currency
    XBC: Currency
    XBD: Currency
    XCD: Currency
    XDR: Currency
    XOF: Currency
    XPD: Currency
    XPF: Currency
    XPT: Currency
    XSU: Currency
    XTS: Currency
    XUA: Currency
    XXX: Currency
    YER: Currency
    ZAR: Currency
    ZMW: Currency
    ZWL: Currency
