# Unit Testing 3 - Solutions

## Exercise 1

Sample `products.py`:

```python
def add_product(products_list):
    new_product_name = input('please input your product name: ')
    if new_product_name not in products_list:
        products_list.append(new_product_name)
    return products_list
```

Sample `test_products.py`:

```python
from unittest.mock import patch
from app import add_product

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

```

## Exercise 2

Sample `users.py`:

```python
from unittest.mock import patch

def get_user_details():
    name = input('Please enter your name: ')
    age = int(input('Please enter your age: '))
    print(f'Thank you, your name is {name} and your age is {age}')
```

Sample `test_users,py`:

```python
@patch('builtins.input')
@patch('builtins.print')
def test_get_user_details(mock_print, mock_input):
    mock_input.side_effect = ['Jane', 25]

    get_user_details()

    mock_print.assert_called_with("Thank you, your name is Jane and your age is 25")
    assert mock_input.call_count == 2
    assert mock_print.call_count == 1
```
