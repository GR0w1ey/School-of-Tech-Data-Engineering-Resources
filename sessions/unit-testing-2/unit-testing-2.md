---
title: Unit Testing 2
---

## Unit Testing 2

---

### Overview

- Dependency Injection
- Mocking
- Intro to `Mock()`

---

### Learning Objectives

- To be able to explain what _Dependency Injection_ is and why we do it.
- To gain experience _Mocking_ in order to write well tested code.

---

### Re-cap - Unit testing

In the previous session we unit-tested a method like this:

```py
def add_two_numbers(num1, num2)
    return num1 + num2
```

Notes:
    Refer back to previous session material & exercises

---

### Consider - Scenario 1

Let's add more complexity to our function, adding a dependency on something else:

```py
from random import randint # generates random numbers

def add_number_and_random(num1):
    return num1 + randint(1, 10)
```

...this adds a dependency to another function.

> What problems might we face testing `add_number_and_random`?

Notes:
    This adds a "dependency"

---

### Consider - Scenario 2

What about this one?!

```py
from random import randint # generates random numbers
def get_random_number():
    return randint(1, 10)

def add_number_and_random(num1)
    return num1 + get_random_number()
```

> What problems might we face testing `get_random_number` or `add_number_and_random`?

Notes:
    Discuss the limits of testing this. We'd have to allow a range of answers, which is not ideal.

---

### Consider - Scenario 2

- When we run `add_number_and_random` is also runs `get_random_number`
- And what if `get_random_number` had it's own dependencies?
- We don't necessarily know (without looking) what `get_random_number` itself is going to depend on
- If we leave it as it is, our test will also indirectly test the dependencies, and dependencies of dependencies, which is _Integration Testing_
- We want to test _only_ the `add_number_and_random` function

---

What happens when our _unit_ depends on the outcome of some other piece of code?
How can we then test our _unit_ in isolation?

Notes:
    This is what the rest of this session is all about!

---

### What is a Dependency

Our _units_ may depend upon other functions, libraries or external services in order to do their job. We call these `dependencies`.

Example dependencies:

- REST API
- MySQL Database
- File Store
- Print / Input / Math etc
- Any more?

---

### How do we do that then?

Can you do dependency injection? If our code can be changed to a useful shape, then:

- <span style="color:green">Yes</span>: Mock it <span style="color:yellow">(Today's topic)</span>

But if not:

- <span style="color:red">No</span>: _Patch_ it, then _Mock_ it (For which see Unit Testing 3)

---

### Dependency Injection (DI)

By _injecting_ the _dependency_, the caller of our function is responsible for providing the `get_random_number` logic:

```py
from random import randint
def get_random_number():
    return randint(1, 10)

def add_number_and_random(num1, generator_function)
    return num1 + generator_function()

# to call it we would use:
print(add_number_and_random(123, get_random_number))
```

Notes:
    Please take a few moments and think how this change (DI) is going to help us with testing?

---

### Which means that

- When we call `add_number_and_random` in our application, we inject the real `get_random_number` function
- When we call `add_number_and_random` in our test, we inject a fake (_mock_) `get_random_number` function

---

### Another example

> Lets look at example using an external API to load some data.

---

Here's a function that calls out to an external service:

```py
def get_todays_price_per_cake():
    api_url = "https://www.random.org/integers/?num=1&min=5&max=10&col=1&base=10&format=plain&rnd=new"
    response = requests.get(api_url)
    if response.status_code == 200:
        return json.loads(response.content)[0]
    else:
        return None
```

---

Here's a function using it to calculate todays cost of a box of cakes, yummy:

```python
def get_price_of_box(number_of_cakes):
    price_per_cake = get_todays_price_per_cake() # Execute dependency
    return number_of_cakes * price_per_cake

print(get_price_of_box(15))
```

Notes:
    Ask:

    - What do we think this code is doing at a high level?
    - Why would it be bad to use an external service? (the service may actually be no longer available, which is a good example of the possible downsides)
    - Run it several times, see the changes in result?

    Points:

    - Main reason: Control. Using an external service, we depend on data that is out of our control for our test.
    - In this particular case the API will return the same data each time, but what if it didn't? For example an API which provides recent news articles.
    - Other reasons: Test execution speed, Test parallelisation, Cost to use external API, API Credential management complexity, Service usage limits...

---

### With dependency injection

Lets reorganise that to use DI (dependency injection):

```python
def get_price_of_box(number_of_cakes, price_getter):
    price_per_cake = price_getter() # Execute dependency
    return number_of_cakes * price_per_cake

print(get_price_of_box(15, get_todays_price_per_cake))
```

---

### The Mock Function

There are two common uses of the word _Mock_, and this can get a bit confusing:

- A Mock function you write yourself
    - These are also called "dummy" functions, which can help disambiguate
- Using the `Mock()` testing tool (more on this later)

---

### The Mock or "Dummy" Function

We make a function (in our test file) that takes the place of the real dependency:

```py
def mock_price_per_cake():
    return 7

# or just as common is
def dummy_price_per_cake():
    return 7
```

Notes:
    Ask:
    - How much data SHOULD we return here?
    - Depends what we are trying to test. In many cases, just the single data point we need might be enough
    - If the test is to ensure the correct country is chosen from the list then we could add more to help guard against a naive edge-case implementation, e.g. that just returns the first from the list

---

### Emoji Check:

Do you feel you understand the need for dependency injection? Say so if not!

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

### Code-Along Example 1 (10 mins)

> Let's write a unit test for `get_price_of_box`, using a "dummy function" we write ourselves
>
> Lets open VSCode and do this together

Notes:

- Solution on next slide
- Can do this exercise as a demo or code-along
- Explain Dependency Injection as a design pattern. (Also called Dependency Inversion or Inversion of Control)  Gives caller control of dependencies. Dependencies are made explicit as they are described in the contract (function or method signature)
- White Box vs Black Box testing
- Unit testing is very strictly a White Box test - we CAN and absolutely do need to look at the internals to write a good test - and we can refactor the internals to make the test easier
- Demonstrate using Postman or similar to inspect the response data from the API and determine what is required for our test case

---

### Example 1 - Solution

```py
def dummy_price_per_cake():
    return 8

def test_get_price_of_box_happy_case():
    number_cakes = 10
    expected = 80

    result = get_price_of_box(number_cakes, dummy_price_per_cake)

    assert expected == result, f'Expected {expected} but was {result}'
```

Note:
    This is only one of many possible answers of course!

---

### Code Along - Example 2

- Let's try to understand what the `random_list_generator` function does, then refactor it to use DI, and then write unit-tests to verify its functionality

```py
import random

def get_random_number():
    return random.randint(1, 10)

def random_list_generator(n):
    result = []
    for _ in range(n):
        result.append(get_random_number())
    return result
```

Notes:

    - Solution on next slide
    - Can do this exercise as a demo or code-along
    - Ask learners what they think the functions do

---

### Example 2 - Solution (part 1/2)

First we update the `random_list_generator` function to include Dependency Injection:

```py
def random_list_generator(n, random_number_generator):
    result = []
    for _ in range(n):
        result.append(random_number_generator())
    return result
```

---

### Example 2 - Solution (part 2/2)

Then we can provide a mock random number generator for our unit test:

```py
def mock_random_number_generator():
    return 7

def test_random_list_generator():
    list_length = 3

    expected = [7, 7, 7]

    result = random_list_generator(list_length,
                                   mock_random_number_generator)

    assert expected == result, f'Expected {expected} but was {result}'
```

---

### Some Caveats of DI

- May require restructuring of your code if retro-fitting
- Tests will be so easy to write you may die of boredom
- Your colleagues will be envious of you
- Recruiters will keep blowing up your phone

---

### Exercise prep

> Instructor to give out the zip file of exercises for `unit-testing-2`
>
> Everyone please unzip the file

---

### Exercise time

> From the zip, you should have a file `exercises/unit-testing-2-numbers-exercise.md`
>
> Let's all do the exercises included in this file
>
> If you finish early, have a look at the file `exercises/unit-testing-2-countries-exercise.md`

---

### Emoji Check:

How did the exercises go? Is dependency injection making more sense now?

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

### Improving our approach

Writing our own mock functions works, but we'd likely have to:

- Create individual mock functions for each test case<!-- .element: class="fragment" -->
- Modify each one to return the desired result<!-- .element: class="fragment" -->

---

### Is there a better way?

What about tools from the testing Frameworks?<!-- .element: class="fragment" -->

---

### Mock()

- The `unittest` framework has a `Mock` function
- `Mock()` allows us to create a new object which we can use to replace dependencies in our code
- We can use it to mock primitive functions or entire modules without having to be fully aware of the underlying architecture of the thing we're trying to mock
- Each method / function call is automagically replaced with another `Mock()` object whenever our _unit_ tries to access it.

---

### Using the Mock utility ⚙️

We import the utility from the `unittest` library - this comes with `pytest`:

```python
from unittest.mock import Mock
```

---

### Configuring our Mock ⚙️

`Mock()`

- `return_value`: Specifies the return value when the mock is called (_stub_)
- `side_effect`: Specifies some other function when the mock is called. For example: Raise an `Exception` when testing an unhappy path

Notes:

Side effect example:

```py
from unittest.mock import Mock
mock = Mock(side_effect=KeyError('foo'))
mock()
Traceback (most recent call last):
 ...
KeyError: 'foo'
```

---

### Example

```py
from unittest.mock import Mock

# Mocking a Function
mock_function = Mock()
mock_function.return_value = 123
print(mock_function()) # 123

# Mocking a Class / Object
mock_class = Mock()
mock_class.some_method.return_value = "Hello World!"
mock_class.some_other_method.return_value = True
# etc...
```

---

### Example Implementation

```python
# Function to be tested
def add_two_numbers(a, random_number_getter_function):
    return a + random_number_getter_function()
```

```python
# With Mock
from unittest.mock import Mock

def test_add_two_numbers():
    # Creates a new mock instance
    mock_get_random_number = Mock()
    mock_get_random_number.return_value = 5

    expected = 10
    actual = add_two_numbers(5, mock_get_random_number)
    assert expected == actual, f'Expected {expected} but was {actual}'
```

Notes:
Point out:

- The use of the `Mock()` class to create a new `object`
- The use of the `return_value` method to specify the return value of the mock when it is called

---

### Spying on our Mock 🕵️

The test tools record the behaviour of our mocks (how they are called, or not) and it's parameters, which we can use later to make better assertions. We can thus "spy" on what happened in our code:

`Mock()`

- `call_count`: Returns the amount of times the mock has been called
- `called_with`: Returns the parameters passed into the mock when called
- `called`: Returns a `bool` indicating if the mock has been called or not

---

### Example

```py
mock_function = Mock()
mock_function.return_value = True
mock_function() # True
mock_function.call_count # 1
```

---

### Making Assertions ✔️

`Mock()`

- `assert_called()`: Fails if mock is not called
- `assert_not_called()`: Fails if mock is called
- `assert_called_with(*args)`: Fails if the mock is not called with the specified params
- `reset_mock()`: Resets mock back to the initial state. Useful if testing one mock under multiple scenarios

---

### Example

```py
mock_function = Mock()
mock_function.return_value = True
mock_function() # True
mock_function.call_count # 1
mock_function() # True
mock_function.reset_mock()
mock_function.assert_called() # Fails
```

---

### Emoji Check:

Do you feel you understand the Mock function? Say so if not!

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

### Example 1 - Refactor

- Try to write a unit-test for `get_price_of_box`. Use unittest's `Mock` class in your tests.

Notes:

- Solution on next slide
- Can do this exercise as a demo or code-along
- Explain that using `Mock()` means we no longer need to define a function for each test case

---

### Example 1 - Refactor Solution

We no longer need to create a separate mock function.

```py
from unittest.mock import Mock

def test_get_price_of_box_happy_case():
    number_cakes = 10
    mock_get_price = Mock() # Mock created as part of unit test
    mock_get_price.return_value = 9

    expected = 90
    result = get_price_of_box(number_cakes, mock_get_price)

    assert expected == result, f'Expected {expected} but was {result}'
    mock_get_price.assert_called() # Can spy on the mock
```

---

### Example 2 - Refactor

- Try to do DI and then write unit-tests for this function (use `Mock` class)

```py
import random

def random_list_generator(n):
    result = []
    for _ in range(n):
        result.append(random.randint(1, 10))
    return result

```

Notes:

- Solution on next slides
- Can do this exercise as a demo or code-along
- This time the random number generation is using the `random` python package.
- Use an example similar to the mocked class to create a `mocked_random.randint` method.

---

### Example 2 - Refactor Solution

First we update the `random_list_generator` function to include Dependency Injection again for the `random` module:

```py
import random

def random_list_generator(n, random_module):
    result = []
    for _ in range(n):
        result.append(random_module.randint(1, 10))
    return result
```

To actually call this function, we could for example use:

```py
random_list_generator(6, random)
```

---

### Example 2 - Refactor Solution

Then we can provide a mock random module for our unit test:

```py
from unittest.mock import Mock

def test_random_list_generator():
    list_size = 4

    mocked_random = Mock()
    # This time we add a return_value on the
    # randint method of our mock
    mocked_random.randint.return_value = 3

    expected = [3, 3, 3, 3]

    result = random_list_generator(list_size, mocked_random)

    assert result == expected
    mocked_random.randint.assert_called()
```

---

### Exercise time (Optional extra)

> Go back over your solutions from Unit Testing 1 (the previous session) and use `Mock()` instead.

---

### Emoji Check:

How did the exercises go? Is Mock making more sense now?

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

### Terms and Definitions - recap

- `Mock`: A piece of _fake_ code standing in to replace some _real_ code.
- `Stub`: Dummy data serving to replace real data usually returned from an external source.
- `Dependency`: A piece of code relied upon by another piece of code.
- `Dependency Injection`: A Software Development paradigm in which dependencies are passed as inputs into the function/class that invokes them.
- `Spy`: examining how a Mock was used to check if our code did the right thing

---

### Overview - recap

- Dependency Injection
- Mocking
- Intro to `Mock()`

---

### Learning Objectives - recap

- To be able to explain what _Dependency Injection_ is and why we do it.
- To gain experience _Mocking_ in order to write well tested code.

---

### Further Reading

- YouTube: [Dependency Injection (in JavaScript but still a great watch)](https://youtu.be/0X1Ns2NRfks)
- [Dependency Injection](https://python-dependency-injector.ets-labs.org/introduction/di_in_python.html)
- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)

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
