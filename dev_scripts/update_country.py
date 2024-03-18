#!/usr/bin/env python
from __future__ import annotations

import json
from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup, Tag


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


def parse_country(country: Tag) -> dict[str, Any]:
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

    countries: dict[str, Any] = {}
    for country in soup.find("table", {"role": "grid"}).find("tbody").find_all("tr"):
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
