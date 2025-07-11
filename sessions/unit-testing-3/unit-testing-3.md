---

title: Unit Testing 3

---

## Unit Testing 3

---

### Overview

- Intro to `patch()`
- Exercise

---

### Learning Objectives

- Know how to use an alternative approach to Dependency Injection

---

### Re-cap

- In the first session we learned how to write some basic unit-tests for our `add_two_numbers` function.
- In the second session we learned how to inject _functional_ dependencies and mock their return values with stubbed data.

---

### How do we do that then?

Can you do dependency injection?

- <span style="color:green">Yes</span>: Mock it <span style="color:grey">(Last session's topic)</span>
- <span style="color:red">No</span>: Patch it, then Mock it <span style="color:yellow">(Today's topic)</span>

---

### What if we don't use Dependency Injection

There are common scenarios where mocking or refactoring for dependency injection aren't always possible, for example:

- We have a legacy app and don't have the resources to restructure it for DI
- We only want to inject certain dependencies, but not built-ins like `print` or `input`

Notes:
    Injecting `print` and `input` all over the place is a pain, we'll show them how to `patch` those functions instead.

---

### `patch()`

> `patch()` allows us to mock a dependency when we can't, or choose not to, inject it.

- It works by intercepting calls to the dependency we've patched and replacing it with a `Mock()` for us
- In order to use it we have to _decorate_ our test with `patch()`
- The mocks are then available to configure the behaviour, to use for spying, and making assertions

Notes:

Will see an example of a decorator in a couple slides using `patch`.

Explain that decorating a function means to apply another function as a bolt-on/"wrapper", which will add extra functionality to extend the original one.

---

### Example 1

How could I test these functions without any modification?

```py
import time

def api_call():
    time.sleep(3)
    return 9

def slow_function_with_DI(value, func_to_call):
    result = value * func_to_call()
    return result

def slow_function_without_DI(value):
    result = value * api_call()
    return result
```

Notes:

Can show an example of testing `slow_function_with_DI` using Mock() as before as a recap.

---

### Example 1 - Solution

```py
from unittest.mock import Mock, patch
from app import slow_function_without_DI

@patch('app.api_call')
def test_slow_function_without_DI(mock_api_call):
    # assemble
    mock_api_call.return_value = 500
    expected = 100 * 500

    # act
    actual = slow_function_without_DI(100)

    # assert
    assert expected == actual
```

---

### Example 2

How could I test this function?

```py
# Without DI
def hello_to_you(name):
    print(f"Hello, {name}!") # Dependency
```

Notes:

Ask why we perhaps don't want to do DI? i.e. built-in function

---

### Example 2 - answer

```py
from unittest.mock import patch

@patch("builtins.print")
def test_prints_hello_to_you(mock_print):
    # Arrange
    my_name = "John"
    expected = "Hello, John!"

    # Act
    hello_to_you(my_name)

    # Assert
    mock_print.assert_called_with(expected) # Passes
```

Notes:

Just for the sake of running this function consider `print = mock_print`

---

### Example 3

How could I test this function?

```py
# Without DI
def greeting():
    name = input("what is your name? ") # Dependency
    return 'Nice to meet you, ' + name
```

---

### Example 3 - answer

```py
from unittest.mock import patch

@patch("builtins.input")
def test_greeting(mock_input):
    # Arrange
    mock_input.return_value = 'Jessica'
    expected = 'Nice to meet you, Jessica'

    # Act
    actual = greeting()

    # Assert
    assert actual == expected
    assert mock_input.call_count == 1
```

Notes:
    N/A

---

### Exercise (code-along)

> Let's all write a test to verify functionality of the following function for this scenario:

Example data:

```text
    price_list = [10, 20]
    user input = 50
    expected_result = [10, 20, 50]
```

```py
def add_price(price_list): # No DI
    value = int(input("Please enter a number: ")) # Dependency
    price_list.append(value)
    return price_list
```

Notes:

Ask them to explain what is happening.

Highlight that the part of the function doing int(input(...)) is very relatable to their mini project work (menu options).

Point out that in reality they need to write this function themselves.

Wait a few minutes for them to try!

After finishing the first test case, ask them to add complexity, ignore the input if it is already available in price list. Tests to verify it's functionality for both scenarios.

---

### Solution (Part 1)

```py
from unittest.mock import patch
from price_lister import add_price

@patch('builtins.input')
def test_add_price(mock_input):
    price_list = [10, 20]
    mock_input.return_value = 50
    expected = [10, 20, 50]

    result = add_price(price_list)

    assert expected == result
```

---

### Solution (Part 2)

> Bonus functionality - "ignore the input if it is already available in price list"

First we write a unit test that considers this case:

```py
from unittest.mock import patch
from price_lister import add_price

@patch('builtins.input')
def test_add_price_already_in_list(mock_input):
    price_list = [10, 20]
    mock_input.return_value = 20
    expected = [10, 20]

    result = add_price(price_list)

    assert expected == result
```

---

### Solution (Part 2)

> Bonus functionality - "ignore the input if it is already available in price list"

Then we can update our `add_price` function to pass the new test:

```py
def add_price(price_list):
    value = int(input("Please enter a number: "))
    if value not in price_list:
        price_list.append(value)
    return price_list
```

---

### Emoji Check:

Do you feel you understand what patching is? Say so if not!

1. 😢 Haven't a clue, please help!
2. 🙁 I'm starting to get it but need to go over some of it please
3. 😐 Ok. With a bit of help and practice, yes
4. 🙂 Yes, with team collaboration could try it
5. 😀 Yes, enough to start working on it collaboratively

Notes:
The phrasing is such that all answers invite collaborative effort, none require solo knowledge.

The 1-5 are looking at (a) understanding of content and (b) readiness to practice the thing being covered, so:

1. 😢 Haven't a clue what's being discussed, so I certainly can't start practising it (play MC Hammer song)
2. 🙁 I'm starting to get it but need more clarity before I'm ready to begin practising it with others
3. 😐 I understand enough to begin practising it with others in a really basic way
4. 🙂 I understand a majority of what's being discussed, and I feel ready to practice this with others and begin to deepen the practice
5. 😀 I understand all (or at the majority) of what's being discussed, and I feel ready to practice this in depth with others and explore more advanced areas of the content

---

### Example 5 - Multiple Dependencies

What if we have two dependencies?!

```py
# No DI
def print_name():
    name = input("Please enter your name: ")
    print(f"Hello, {name}!") # Dependency
```

---

### Example 5 - Solution

```py
from unittest.mock import patch

@patch("builtins.input")
@patch("builtins.print")
def test_print_name(mock_print, mock_input):
    # Arrange
    mock_input.return_value = "John"
    expected = "Hello, John!"

    # Act
    print_name()

    # Assert
    mock_print.assert_called_with(expected) # Passes
    assert mock_input.call_count == 1
    assert mock_print.call_count == 1
```

---

### Patching multiple dependencies

Note the order of the `@patch()` decorators compared to the order of the arguments in the test function.

- The first argument for the mock returned from `@patch()` belongs to the patch directly above the function definition (in this example that's `@patch("builtins.print")`).
- It then works up the way, so the second `@patch()` decorator above the function will provide the second argument (in this case `@patch("builtins.input")` is 2 lines above the function definition, so `mock_input` is the second argument).

---

### Configuring our Patch

For example:

- `@patch("path.to.module.method")`
- `@patch("src.module.method")`
- `@patch("builtins.input")`

So:

The path to the function to be patched is provided as a string to `@patch()`.

The path should match the level which would be needed if the function were to be imported into the file, e.g. `from src.module import method` -> `@patch("src.module.method")`.

---

### Exercise prep

> Instructor to give out the zip file of exercises for `unit-testing-3`
>
> Everyone please unzip the file

---

### Exercise time

> From the zip, you should have a file `exercises/unit-testing-3-exercises.md`
>
> Let's all do the exercises included in this file

---

### Emoji Check:

How did the exercises go? Is patching making more sense now?

1. 😢 Haven't a clue, please help!
2. 🙁 I'm starting to get it but need to go over some of it please
3. 😐 Ok. With a bit of help and practice, yes
4. 🙂 Yes, with team collaboration could try it
5. 😀 Yes, enough to start working on it collaboratively

Notes:

The phrasing is such that all answers invite collaborative effort, none require solo knowledge.

The 1-5 are looking at (a) understanding of content and (b) readiness to practice the thing being covered, so:

1. 😢 Haven't a clue what's being discussed, so I certainly can't start practising it (play MC Hammer song)
2. 🙁 I'm starting to get it but need more clarity before I'm ready to begin practising it with others
3. 😐 I understand enough to begin practising it with others in a really basic way
4. 🙂 I understand a majority of what's being discussed, and I feel ready to practice this with others and begin to deepen the practice
5. 😀 I understand all (or at the majority) of what's being discussed, and I feel ready to practice this in depth with others and explore more advanced areas of the content

---

### Patching Gotcha - Where to Patch

Imagine you have a project with the following structure (two modules):

```py
# module_a.py
def add_nums(a, b):
    return a + b
```

and

```py
# module_b.py
from module_a import add_nums

def do_maths(a, b):
    print(add_nums(a, b))
```

If you wanted to unit test `do_maths` from `module_b.py`, you would need to patch `add_nums`. But...

---

### Patching Gotcha - Where to Patch

It would be tempting to write the patch for where `add_nums` was created, e.g.:

```py
@patch('module_a.add_nums') # Incorrect
def test_do_maths():
    ...
```

However, as `module_b` has imported `add_nums`, you have to patch `add_nums` where it is used, **NOT** where it is defined, e.g.:

```py
@patch('module_b.add_nums') # Correct
def test_do_maths():
    ...
```

See [the documentation](https://docs.python.org/3/library/unittest.mock.html#where-to-patch) for some more examples of this and similar situations.

---

### Terms and Definitions - recap

- `Mock`: A piece of _fake_ code standing in to replace some _real_ code.
- `Stub`: Dummy data serving to replace real data usually returned from an external source.
- `Dependency`: A piece of code relied upon by another piece of code.
- `Dependency Injection`: A Software Development paradigm in which dependencies are passed as inputs into the function or class which invokes them.

---

### Overview - recap

- Intro to `patch()`
- Exercise

---

### Learning Objectives - recap

- Know how to use an alternative approach to Dependency Injection

---

### Further Reading

- [Dependency Injection](https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html)
- Handbook: [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)

---

### Emoji Check:

On a high level, do you think you understand the main concepts of this session? Say so if not!

1. 😢 Haven't a clue, please help!
2. 🙁 I'm starting to get it but need to go over some of it please
3. 😐 Ok. With a bit of help and practice, yes
4. 🙂 Yes, with team collaboration could try it
5. 😀 Yes, enough to start working on it collaboratively

Notes:

The phrasing is such that all answers invite collaborative effort, none require solo knowledge.

The 1-5 are looking at (a) understanding of content and (b) readiness to practice the thing being covered, so:

1. 😢 Haven't a clue what's being discussed, so I certainly can't start practising it (play MC Hammer song)
2. 🙁 I'm starting to get it but need more clarity before I'm ready to begin practising it with others
3. 😐 I understand enough to begin practising it with others in a really basic way
4. 🙂 I understand a majority of what's being discussed, and I feel ready to practice this with others and begin to deepen the practice
5. 😀 I understand all (or at the majority) of what's being discussed, and I feel ready to practice this in depth with others and explore more advanced areas of the content
