#!/usr/bin/env python
from __future__ import annotations

import json
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import TypedDict

from bs4 import BeautifulSoup, Tag


class CountryDict(TypedDict):
    alpha_2_code: str
    alpha_3_code: str
    english_name: str
    french_name: str
    numeric_code: int


def clean_nbsp(text: str) -> str:
    return text.replace("\u00a0", " ").strip()


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument(
        "--definitions",
        type=Path,
        help="html with country definitions",
        required=True,
    )
    return parser.parse_args()


def get_tag(tag: Tag, name: str, attributes: dict[str, str] | None = None) -> Tag:
    attributes = attributes or {}
    found = tag.find(name, attrs=attributes)
    if not isinstance(found, Tag):
        msg = f"Tag `{name}` not found in `{tag}`"
        raise TypeError(msg)
    return found


def parse_country(country: Tag) -> CountryDict:
    attributes = [td.get_text() for td in country.find_all("td")]
    return {
        "alpha_2_code": attributes[2],
        "alpha_3_code": attributes[3],
        "english_name": clean_nbsp(attributes[0]),
        "french_name": clean_nbsp(attributes[1]),
        "numeric_code": int(attributes[4]),
    }


def update_country(definitions: Path) -> None:
    data_path = Path("__file__").parent.joinpath("src/teritorio/_data/country.json")
    soup = BeautifulSoup(definitions.read_text(), "lxml")

    countries: dict[str, CountryDict] = {}
    table = get_tag(soup, "table", {"role": "grid"})
    for country in get_tag(table, "tbody").find_all("tr"):
        parsed_country = parse_country(country)
        countries[parsed_country["alpha_3_code"]] = parsed_country

    with data_path.open("w") as file:
        json.dump(countries, file, indent=4, sort_keys=True)

    with data_path.open("a") as file:
        file.write("\n")


def main() -> None:
    args = parse_args()
    update_country(args.definitions)


if __name__ == "__main__":
    main()
