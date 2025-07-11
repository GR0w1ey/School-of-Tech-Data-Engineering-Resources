from unittest.mock import Mock
from country_info import get_country_code, get_country_currency, transform, show_country_info

def test_get_country_code():
  # Arrange
  test_countries = [
    {"name": "United Kingdom", "alpha3Code": "UK"},
    {"name": "United States", "alpha3Code": "USA"}
  ]
  test_name = "United Kingdom"
  expected = "UK"

  # Act 
  actual = get_country(test_countries, test_name)

  # Assert
  assert expected == actual


def test_get_country_currency():
  # Arrange
  test_countries = [
        {"name": "United Kingdom", "currencies": [{"code": "GBP"}]},
        {"name": "United States", "currencies": [{"code": "USD"}]}
    ]
  test_name = "United Kingdom"
  expected = "GBP"

  # Act
  actual = get_country_currency(test_countries, test_name)

  # Assert
  assert expected == actual


def test_transform():
  # Assemble
  mock_get_countries = Mock()
  mock_get_countries.return_value = [{"name": "United Kingdom", "alpha3Code": "UK", "currencies": [{"code": "GBP"}]}]

  mock_get_country_code = Mock()
  mock_get_country_code.return_value = 'UK'

  mock_get_country_currency = Mock()
  mock_get_country_currency.return_value = 'GBP'

  test_name = "United Kingdom"
  expected = {"name": "United Kingdom", "country_code": "UK", "currency_code": "GBP"}
  
  # Act
  actual = transform(test_name, mock_get_countries,
                    mock_get_country_code, mock_get_country_currency)
  
  assert actual == expected

def test_show_country_info():
  # Assemble
  mock_get_countries = Mock()
  mock_get_countires.return_value = [{"name": "United Kingdom", "alpha3Code": "UK", "currencies": [{"code": "GBP"}]}]

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
