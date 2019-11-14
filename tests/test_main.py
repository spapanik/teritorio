from teritorio import main


class TestCountries:
    countries = main.Countries()

    def test_specific_country(self):
        usa = self.countries.USA
        assert usa == self.countries["USA"]
        assert usa.english_name == "United States of America (the)"
        assert usa.french_name == "États-Unis d'Amérique (les)"
        assert usa.alpha_2_code == "US"
        assert usa.alpha_3_code == "USA"
        assert usa.numeric_code == 840

    def test_number_of_countries(self):
        assert len(self.countries) == 249

    def test_singleton(self):
        countries = main.Countries()

        assert self.countries == countries


class TestCurrencies:
    currencies = main.Currencies()

    def test_specific_currency(self):
        jpy = self.currencies.JPY
        assert jpy == self.currencies["JPY"]
        assert jpy.code == "JPY"
        assert jpy.name == "Yen"
        assert jpy.entities == ["JAPAN"]
        assert jpy.numeric_code == 392
        assert jpy.minor_units == 0

    def test_number_of_currencies(self):
        assert len(self.currencies) == 179

    def test_singleton(self):
        currencies = main.Currencies()

        assert self.currencies == currencies
