from unittest.mock import patch
from products import add_product

@patch('builtins.input')
def test_can_ignore_already_available_product(mock_input):
    mock_input.return_value = 'Pizza'
    products_list = ['Pizza', 'Soup']

    predicted = ['Pizza', 'Soup']

    actual = add_product(products_list)

    assert actual == predicted

@patch('builtins.input')
def test_can_add_new_product(mock_input):
    mock_input.return_value = 'Pizza'
    products_list = ['Soup']

    predicted = ['Soup', 'Pizza']

    actual = add_product(products_list)

    assert actual == predicted
