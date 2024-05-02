# Usage

`teritorio` has two iterable singletons: `Countries` and `Currencies`,
and two dataclasses: `Country` and `Currency`, that represent a specific
country or currency. `Countries` and `Currencies` are importable from
teritorio.

`Countries` and `Currencies`, as they are singletons, can be
instantiated more than once with negligible performance penalty.

## Countries

`Countries` is an iterable of all countries

Example usage of the `Countries` class.

```python
from teritorio import Countries

# list all countries
for country in Countries():
    print(country)

# get a specific country
countries = Countries()

# access the country as an attribute
print(countries.DEU)
# prints Country(english_name='Germany', french_name="Allemagne (l')", alpha_2_code='DE', alpha_3_code='DEU', numeric_code=276)

# access the country with square brackets
print(countries["DEU"])
# prints Country(english_name='Germany', french_name="Allemagne (l')", alpha_2_code='DE', alpha_3_code='DEU', numeric_code=276)
```

## Currencies

`Currencies` is an iterable of all currencies

Example usage of the `Currencies` class.

```python
from teritorio import Currencies

# list all currencies
for currency in Currencies():
    print(currency)

# get a specific currency
currencies = Currencies()

# access the currency as an attribute
print(currencies.GBP)
# print Currency(code='GBP', name='Pound Sterling', entities=('GUERNSEY', 'ISLE OF MAN', 'JERSEY', 'UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND (THE)'), numeric_code=826, minor_units=2)

# access the currency with square brackets
print(currencies["GBP"])
# prints Currency(code='GBP', name='Pound Sterling', entities=('GUERNSEY', 'ISLE OF MAN', 'JERSEY', 'UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND (THE)'), numeric_code=826, minor_units=2)
```
