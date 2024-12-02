#!/usr/bin/env python
from __future__ import annotations

import json
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import TypedDict

from bs4 import BeautifulSoup, Tag


class CurrencyDict(TypedDict):
    code: str
    entities: list[str]
    minor_units: int | None
    name: str
    numeric_code: int


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "--definitions",
        type=Path,
        help="xml with currency definitions",
        required=True,
    )
    return parser.parse_args()


def get_tag(tag: Tag, name: str) -> Tag:
    found = tag.find(name)
    if not isinstance(found, Tag):
        msg = f"Tag `{name}` not found in `{tag}`"
        raise TypeError(msg)
    return found


def parse_currency(currency: Tag) -> CurrencyDict | None:
    code = currency.find("Ccy")
    if not code:
        return None

    minor_units_text = get_tag(currency, "CcyMnrUnts").get_text()
    try:
        minor_units = int(minor_units_text)
    except ValueError:
        minor_units = None

    return {
        "code": code.get_text().strip(),
        "entities": [get_tag(currency, "CtryNm").get_text().strip()],
        "minor_units": minor_units,
        "name": get_tag(currency, "CcyNm").get_text().strip(),
        "numeric_code": int(get_tag(currency, "CcyNbr").get_text()),
    }


def update_currency(definitions: Path) -> None:
    data_path = Path("__file__").parent.joinpath("src/teritorio/_data/currency.json")
    soup = BeautifulSoup(definitions.read_text(), features="xml")

    currencies: dict[str, CurrencyDict] = {}
    for currency in get_tag(soup, "CcyTbl").find_all("CcyNtry"):
        parsed_currency = parse_currency(currency)
        if parsed_currency is not None:
            if parsed_currency["code"] in currencies:
                currencies[parsed_currency["code"]]["entities"].extend(
                    parsed_currency["entities"]
                )
                currencies[parsed_currency["code"]]["entities"].sort()
            else:
                currencies[parsed_currency["code"]] = parsed_currency

    with data_path.open("w") as file:
        json.dump(currencies, file, indent=4, sort_keys=True)

    with data_path.open("a") as file:
        file.write("\n")


def main() -> None:
    args = parse_args()
    update_currency(args.definitions)


if __name__ == "__main__":
    main()
