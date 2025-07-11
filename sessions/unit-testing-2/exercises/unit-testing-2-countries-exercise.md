# Unit-Testing 2: Mocking and Stubbing with Dependency Injection

1. Open the file `country_info.py` from the `handouts` folder
1. Run the `country_info.py` file to check it works
1. Write unit-tests in a file called `test_country_info.py` for
   1. `get_country_code`
   1. `get_country_currency`
   1. `transform`
   1. `show_country_info`
1. As you write each test, run them often with the `pytest` module

## Think about

- Where will you need to refactor the code to inject dependencies?
- Which dependencies will require mocks, and which will not?
- Are you testing happy/sad paths? common/corner/edge cases?
- How does unit-testing improve the code?

## STRETCH

Try to use unittest's `Mock` class in your tests.
