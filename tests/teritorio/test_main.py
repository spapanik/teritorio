from __future__ import annotations

from typing import TypeVar, Union

import pytest

from teritorio import main

TERITORIO_CLASS = TypeVar(
    "TERITORIO_CLASS", bound=Union[type[main.Countries], type[main.Currencies]]
)


class TestCountries:
    countries = main.Countries()

    def test_str(self) -> None:
        expected_str = "Countries()"
        assert expected_str == str(self.countries)
        assert expected_str == repr(self.countries)

    def test_iter(self) -> None:
        assert list(self.countries) == list(iter(self.countries))

    def test_specific_country(self) -> None:
        usa = self.countries.USA
        assert usa == self.countries["USA"]
        assert usa.english_name == "United States of America (the)"
        assert usa.french_name == "États-Unis d'Amérique (les)"
        assert usa.alpha_2_code == "US"
        assert usa.alpha_3_code == "USA"
        assert usa.numeric_code == 840

    def test_number_of_countries(self) -> None:
        expected_number = 249
        assert expected_number == len(self.countries)
        assert expected_number == len(list(self.countries))

    def test_singleton(self) -> None:
        countries = main.Countries()

        assert self.countries == countries


class TestCurrencies:
    currencies = main.Currencies()

    def test_str(self) -> None:
        expected_str = "Currencies()"
        assert expected_str == str(self.currencies)
        assert expected_str == repr(self.currencies)

    def test_iter(self) -> None:
        assert list(self.currencies) == list(iter(self.currencies))

    def test_specific_currency(self) -> None:
        jpy = self.currencies.JPY
        assert jpy == self.currencies["JPY"]
        assert jpy.code == "JPY"
        assert jpy.name == "Yen"
        assert jpy.entities == ("JAPAN",)
        assert jpy.numeric_code == 392
        assert jpy.minor_units == 0

    def test_number_of_currencies(self) -> None:
        expected_number = 179
        assert expected_number == len(self.currencies)
        assert expected_number == len(list(self.currencies))

    def test_singleton(self) -> None:
        currencies = main.Currencies()

        assert self.currencies == currencies


@pytest.mark.parametrize("class_", [main.Currencies, main.Countries])
def test_hashable(class_: TERITORIO_CLASS) -> None:
    obj = next(iter(class_()))
    assert len({obj: "test"}) == 1
