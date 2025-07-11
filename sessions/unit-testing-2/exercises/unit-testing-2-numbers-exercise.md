# Unit Testing 2 Exercises

This recaps info from the slides and previous session (i.e. is very similar on purpose).

1. Write a unit test for the below function.

    ```py
    def add_two_numbers(a, b):
        return a + b
    ```

2. Write a unit test for the below function `add_number_with_random_number`. You will need to update the code to make use of **dependency injection**, and create a mock function.

    ```py
    import random
    def get_random_number():
        return random.randint(1, 10)

    def add_number_with_random_number(a):
        return a + get_random_number()
    ```

3. Write a unit test for the below function `add_two_random_numbers`. You will need to update the code to make use of **dependency injection** and create a mock function.

    ```py
    from random import randint

    def get_random_number():
        return randint(1, 10)

    def add_two_random_numbers():
        return get_random_number() + get_random_number()
    ```

4. Write a unit test for the below function `get_random_number`. This time it's slightly different as we need to mock a function we haven't written, but the same principles apply. Hint: you need to match the number of arguments that the `randint` function takes for the mock function you will write.

    ```py
    from random import randint

    def get_random_number():
        return randint(1, 10)
    ```
