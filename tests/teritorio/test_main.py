from teritorio import main


class TestCountries:
    countries = main.Countries()

    def test_specific_country(self) -> None:
        usa = self.countries.USA  # type: ignore[attr-defined]
        assert usa == self.countries["USA"]
        assert usa.english_name == "United States of America (the)"
        assert usa.french_name == "États-Unis d'Amérique (les)"
        assert usa.alpha_2_code == "US"
        assert usa.alpha_3_code == "USA"
        assert usa.numeric_code == 840

    def test_number_of_countries(self) -> None:
        assert len(self.countries) == 249

    def test_singleton(self) -> None:
        countries = main.Countries()

        assert self.countries == countries


class TestCurrencies:
    currencies = main.Currencies()

    def test_specific_currency(self) -> None:
        jpy = self.currencies.JPY  # type: ignore[attr-defined]
        assert jpy == self.currencies["JPY"]
        assert jpy.code == "JPY"
        assert jpy.name == "Yen"
        assert jpy.entities == ["JAPAN"]
        assert jpy.numeric_code == 392
        assert jpy.minor_units == 0

    def test_number_of_currencies(self) -> None:
        assert len(self.currencies) == 180

    def test_singleton(self) -> None:
        currencies = main.Currencies()

        assert self.currencies == currencies
