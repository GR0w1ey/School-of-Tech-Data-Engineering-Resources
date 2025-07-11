from unittest.mock import Mock
from exercise_2_country_info import get_country_code, get_country_currency, show_country_info, transform

# One common case for the happy path defined below for each function - additional cases could be added to test unhappy path & corner/edge cases

def test_get_country_code():
    test_countries = [
        {"name": "United Kingdom", "alpha3Code": "UK"},
        {"name": "United States", "alpha3Code": "USA"}
    ]

    test_name = "United Kingdom"
    expected = "UK"
    actual = get_country_code(test_countries, test_name)

    assert expected == actual

def test_get_country_currency():
    test_countries = [
        {"name": "United Kingdom", "currencies": [{"code": "GBP"}]},
        {"name": "United States", "currencies": [{"code": "USD"}]}
    ]

    test_name = "United Kingdom"
    expected = "GBP"
    actual = get_country_currency(test_countries, test_name)

    assert expected == actual

def test_transform():
    mock_get_countries = Mock()
    mock_get_countries.return_value = [{"name": "United Kingdom", "alpha3Code": "UK", "currencies": [{"code": "GBP"}]}]

    mock_get_country_code = Mock()
    mock_get_country_code.return_value = 'UK'

    mock_get_country_currency = Mock()
    mock_get_country_currency.return_value = 'GBP'

    test_name = "United Kingdom"
    expected = {"name": "United Kingdom", "country_code": "UK", "currency_code": "GBP"}
    actual = transform(test_name, mock_get_countries,
                       mock_get_country_code, mock_get_country_currency)

    assert actual == expected

# An example of how to mock print() and check that it has been called
def test_show_country_info():
    # Assemble
    mock_get_countries = Mock()
    mock_get_countries.return_value = [{"name": "United Kingdom", "alpha3Code": "UK", "currencies": [{"code": "GBP"}]}]

    mock_display_countries = Mock()
    mock_display_countries.return_value = [{"name": "United Kingdom", "alpha3Code": "UK", "currencies": [{"code": "GBP"}]}]

    mock_get_country_code = Mock()
    mock_get_country_currency = Mock()

    mock_print = Mock()

    mock_input = Mock()
    mock_input.return_value = 0

    mock_transform = Mock()
    mock_transform.return_value = {"name": "United Kingdom", "country_code": "UK", "currency_code": "GBP"}

    expected = {"name": "United Kingdom", "country_code": "UK", "currency_code": "GBP"}

    # Act
    show_country_info(mock_display_countries, mock_get_countries,
                      mock_get_country_code, mock_get_country_currency,
                      mock_print, mock_input, mock_transform)
    mock_print.assert_called_once_with(expected)
