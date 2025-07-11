# Unit Testing 2 cheatsheet

## Dependency Injection

### Pre Dependency Injection

```python
def get_countries():
    headers = {'Content-Type': 'application/json'}
    api_url = "https://restcountries.com/v2/all"

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_country_code(key):
    countries = get_countries() # Dependency hidden in the function
    return countries[key]

print(get_country_code("GBR", get_countries))
```

### Post Dependency Injection

```python
def get_countries():
    headers = {'Content-Type': 'application/json'}
    api_url = "https://restcountries.com/v2/all"

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

 # Inject get_countries dependency
def get_country_code(key, get_countries):
    countries = get_countries() # Dependency passed in (much easier to test!)
    return countries[key]

print(get_country_code("GBR", get_countries))
```

- When we call `get_country_code` in our application, we inject the real `get_countries` function
- When we call `get_country_code` in our test, we inject a fake (_mock_) `get_countries` function

### Writing Test for Dependency Injection

```python
def test_find_country_capital():
    # Arrange
    expected = {"alpha3Code": "GBR", "capital": "London"}

    def mock_get_countries():
        return [
            {"alpha3Code": "USA", "capital": "Washington DC"},
            {"alpha3Code": "GBR", "capital": "London"},
            {"alpha3Code": "TKM", "capital": "Ashgabat"}
        ]

    # Act
    actual = get_country_code('GBR', mock_get_countries)

    # Assert
    assert actual == expected
```

## Mocking

- `Mock()` creates a Mock object
- `return_value` Specifies the return value when the mock is called (_stub_)
- `side_effect` Specifies some other function when the mock is called.
- `call_count` Returns the amount of times the mock has been called
- `called_with` Returns the parameters passed into the mock when called
- `called` Returns a `bool` indicating if the mock has been called or not

```python
from random import randint
from unittest.mock import Mock

def add_two_numbers(a, randint):
    return a + randint(1, 10)

def test_add_two_numbers():
    # Creates a new mock instance
    mock_get_random_number = Mock()
    mock_get_random_number.return_value = 5

    expected = 10
    actual = add_two_numbers(5, mock_get_random_number)
    assert expected == actual
    assert mock_get_random_number.call_count = 1
    assert mock_get_random_number.called
```

## Mocking Assertions

- `assert_called()` Fails if mock is not called
- `assert_not_called()` Fails if mock is called
- `assert_called_with(*args)` Fails if the mock is not called with the specified params
- `reset_mock()` Resets mock back to the initial state. Useful if testing one mock under multiple scenarios

```python
mock_function = Mock()
mock_function.return_value = True
mock_function() # True
mock_function.call_count # 1
mock_function() # True
mock_function.reset_mock()
mock_function.assert_called() # Fails
```

### Unit Testing Terms and Definitions

- `Mock`: A piece of _fake_ code standing in to replace some _real_ code.
- `Stub`: Dummy data serving to replace real data usually returned from an external source.
- `Dependency`: A piece of code relied upon by another piece of code.
- `Dependency Injection`: A Software Development paradigm in which dependencies are passed as inputs into the function/class that invokes them.
