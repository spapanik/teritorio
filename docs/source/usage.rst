=====
Usage
=====

``teritorio`` has two iterable singletons: ``Countries`` and ``Currencies``, and two dataclasses:
``Country`` and ``Currency``, that represent a specific country or currency. ``Countries`` and ``Currencies``
are importable from teritorio.

``Countries`` and ``Currencies``, as they are singletons, can be instantiated more than once with
negligible performance penalty.

.. py:module:: teritorio.main

Countries
---------

..  py:class:: Countries

   An iterable of all countries

    ..  py:attribute:: XYZ

       The country with 3-letter code XYZ. The same country is accessible via square brackets Countries()["XYZ"]

..  py:class:: Country

    A representation of a specific country.

    ..  py:attribute:: english_name
        :type: str

        The official name of the country in English

    ..  py:attribute:: french_name
        :type: str

        The official name of the country in French

    ..  py:attribute:: alpha_2_code
        :type: str

        The 2 letter code of the country

    ..  py:attribute:: alpha_3_code
        :type: str

        The 3 letter code of the country

    ..  py:attribute:: numeric_code
        :type: int

        The numeric code of the country


Example usage of the ``Countries`` class.

.. code:: python

    from teritorio import Countries

    # list all countries
    for country in Countries():
        print(country)

    # get a specific country
    countries = Countries()

    # access the country as an attribute
    print(countries.DEU)  # Country(english_name='Germany', french_name="Allemagne (l')", alpha_2_code='DE', alpha_3_code='DEU', numeric_code=276)
    # access the country with square brackets
    print(countries["DEU"])  # Country(english_name='Germany', french_name="Allemagne (l')", alpha_2_code='DE', alpha_3_code='DEU', numeric_code=276)


Currencies
----------

..  py:class:: Currencies

   An iterable of all currencies

    ..  py:attribute:: XYZ

       The currency with 3-letter code XYZ. The same currency is accessible via square brackets Currencies()["XYZ"]

..  py:class:: Currency

    A representation of a specific currency.

    ..  py:attribute:: code
        :type: str

        The 3 letter code of the currency

    ..  py:attribute:: name
        :type: str

        The name of the currency

    ..  py:attribute:: entities
        :type: list[str]

        The list of entities (countries) that use this currency

    ..  py:attribute:: numeric_code
        :type: int

        The numeric code of the currency

    ..  py:attribute:: minor_units
        :type: int | None

        The number of decimal digits of this currency, if applicable


Example usage of the ``Currencies`` class.

.. code:: python

    from teritorio import Currencies

    # list all currencies
    for currency in Currencies():
        print(currency)

    # get a specific currency
    currencies = Currencies()

    # access the currency as an attribute
    print(currencies.GBP)  # Currency(code='GBP', name='Pound Sterling', entities=['GUERNSEY', 'ISLE OF MAN', 'JERSEY', 'UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND (THE)'], numeric_code=826, minor_units=2)
    # access the currency with square brackets
    print(currencies["GBP"])  # Currency(code='GBP', name='Pound Sterling', entities=['GUERNSEY', 'ISLE OF MAN', 'JERSEY', 'UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND (THE)'], numeric_code=826, minor_units=2)
