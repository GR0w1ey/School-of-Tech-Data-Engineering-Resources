# Unit Testing 3 Exercises

## Exercise 1

Write a python function named `add_product` that:

- When called, it will ask user to type product name in terminal (using input() function)
- If user writes a product name that already exists in the `products_list` it should return `products_list` without any change
- Otherwise it should add the product name that user entered to the the end of `products_list` and then return the list.

Write at least two unit-tests to verify its functionality for both scenarios.

Hints:

- You need to patch `input` function in your tests
- Put the main code and tests in separate files

The initial implementation of the function is like this:

```py
def add_product(products_list):
    pass
```

## Exercise 2

Write a unit test for the below function. You will need to patch the `input` and `print` function. Assert what the `print` function was called with, and assert how many times the `input` and `print` function were respectively called.

You will need to figure out how to supply two different values for both `input` calls.

```py
def get_user_details():
    name = input('Please enter your name: ')
    age = int(input('Please enter your age: '))
    print(f'Thank you, your name is {name} and your age is {age}')
```

Hint: the side_effect method of Mock() can be used to iterate over different return values each time the mock is called.

```py
mock_input.side_effect = [1, 2, 3]
```
