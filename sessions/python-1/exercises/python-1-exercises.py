"""
# Python 1 Exercises

For these exercises, you can choose to store the answers in one file, or have one file each per exercise. It's up to you.

## Part 1

### Strings

1. Create a variable which will store your first name. Print out the variable.
2. Create a second variable which will store your last name. Concatenate the two variables and print out the result.
3. Extend the above to print the following using an `f-string`: `Hi, my name is {first_name} {last_name}`.
"""

first_name = "Samir"
print(first_name)

last_name = "Shahid"
print(first_name + " " + last_name)

print(f"Hi, my name is {first_name} {last_name}.")

"""
### Integers

1. Create two variables that store integer values. Calculate the product (the number you get by multiplying two or more other numbers together) of the two integers and store it in a third variable. Print the value of this variable.
2. Extend the above to print out the following: `The product of {x} and {y} is {product}`, replacing `x, y, product` with the values for the above.
"""
x = 1
y = 2

product = x * y

print(product)

print(f"The product of {x} and {y} is {product}")

"""
### Lists

For this section, we will be operating on the below list of names. Please copy this line and paste it into your code file. Remember that list indexes start at zero!

```py
people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
```

1. Retrieve the third element (the second-indexed element) and store it in its own variable. Print the variable.
2. Retrieve the element third from the back of the list and store it in its own variable. Print the variable.
3. Split the list into a new list with just the names Mark, Lisa, Joe and Barry.
4. Print whether or not the first and last element in the list are equal to one another.

"""
people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]
stored_element = people[2]
print(stored_element)

third_from_back = people[-3]
print(third_from_back)

sublist_people = people[2:6]
print(sublist_people)

print(people[0] == people[-1])

"""
### Input

Hint: You can use `input()` as many times as you like. For instance, you can ask for someone's first name on one line, and their last name on another line.

1. Accept input from the user for their name. Print their name out.
2. Accept two integer inputs from the user and calculate the product. Print out the product.
3. Accept two integer inputs from the user. Use the comparison operator to print out if the two values are equal (`True`), or if they're not (`False`).

"""
name = input("Please enter your name: ")
print(name)

int_a = int(input("Enter first integer: "))
int_b = int(input("Enter second integer: "))
product = int_a * int_b
print(product)

int_a = int(input("Enter first integer: "))
int_b = int(input("Enter second integer: "))
print(int_a == int_b)

"""
## Part 2

### Input and Numbers

1. Accept an integer input from the user. If the number is even, print out an appropriate message, and vice versa if it is odd.
    1. **Hint**: Using modulus may help you here.
2. Extend the above to print a different message if the number is a multiple of four.
3. Accept an integer input from the user. If the number is a multiple of three, print the word `fizz`. If the number is a multiple of five, print `buzz`. If it is neither then do not print anything.

"""

user_input = int(input("Please enter an integer: "))
if user_input % 4 == 0:
  print("This integer is a multiple of four!")
elif user_input % 2 == 0:
  print("This integer is even!")
else:
  print("This integer is odd!")

user_input = int(input("Please enter an integer: "))
if user_input % 3 == 0:
  print("fizz")
elif user_input % 5:
  print("buzz")

"""
### Temperature Conversion

1. Write a program that will convert celsius to fahrenheit, and vice versa. Accept two inputs from the user. The first will be a letter which is either `c`, which means you should convert from fahrenheit to celsius, or `f` which is vice versa. For the second input, accept an integer value representing the temperature. Print out the converted value, along with the correct temperature type.

- Expected input: `f` and `100`
- Expected output: `100c is 212.0f`
    - Converting from a temperature in fahrenheit (`F`) to celsius, use: `(F - 32) * (5/9)`
    - Converting from a temperature in celsius (`C`) to fahrenheit, use: `(C * 1.8) + 32`

"""

temperature_scale = input("Please enter a temperature scale to convert to (c/f): ")
temperature = int(input("Please enter a temperature to convert: "))

if temperature_scale == 'f':
  print(f"{temperature}c is {(temperature * 1.8) + 32}f")
elif temperature_scale == 'c':
  print(f"{temperature}f is {(temperature - 32) * (5/9)}c")
else:
  print("Please enter valid temperature scale either 'c' or 'f'.")
"""
## Part 3

1. In your own words, describe each of the following logical operators: `and`, `or` and `not`.
2. Consider the below code. Write down what you think the expected output will be.

    ```py
    a = False
    b = False
    x = not(a)
    y = not(b)
    print(a or b)
    print(x or y)
    print(a or x)
    print(x or b)
    ```

3. Consider the below code. Write down what you think the expected output will be.

    ```py
    a = False
    b = False
    x = not(a)
    y = not(b)
    print(a and b)
    print(a and x)
    print(y and b)
    print(x and y)
    ```

4. Without referring back to the slides, write down the truth table for each of the three logical operators.

5. Create a program for the following Bank Loan specification:

> A bank will offer a customer a loan if they are old enough and have a large enough salary. Ask the user for input of both their age and their salary.

- If the user is over 21 and has a salary of at least £21000, offer them a loan of up to £50,000.
- If the user is over 30 and has a salary of at least £35000, offer them a loan of up to £75,000.
- If the user is over 30 and has a salary of at least £50000, offer them a loan of up to £100,000.
- If none of the above, do not offer them a loan.

"""

user_age = int(input("Enter age please: "))
user_salaries = int(input("Enter salary please: "))
if user_age > 30 and user_salary >= 50000:
  print("You are eligible for a loan of up to 100000.")
elif user_age > 30 and user_salary >= 35000:
  print("You are eligible for a loan of up to 35000.")
elif user_age > 21 and user_salary >= 21000:
  print("You are eligible for a loan of up to 21000.")
else:
  print("You are ineligible for a loan.")
