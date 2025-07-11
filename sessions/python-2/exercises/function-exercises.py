# """
# 1. Create a function that takes two numbers as arguments and return the sum. Print the result.
# 2. Extend the above by passing an arbitrary amount of integers to a function and return the result. Print the result. Hint: use *args.
# """
# def calc_sum(*numbers):
#   return sum(numbers)

# print(calc_sum(5, 8, 8, 9, 10))

# # 3. Pass an arbitrary amount of named arguments to a function and create a dictionary. The keys will be the names of the arguments and the values are assigned values of the named arguments. Hint: use **kwargs.
# def dictionary_builder(**kwargs):
#   dictionary = {}

#   for key, value in kwargs.items():
#     dictionary[key] = value

#   return dictionary

# new_dict = dictionary_builder(name = "Gregor", age = 25, occupation = "Packaged App Development Analyst")
# print(new_dict)

"""
Bonus - basic calculator
1. Create a scientific/basic calculator that makes use of separate functions to perform calculations, such as: add, divide, area_of_a_circle etc...
2. Add some form of user interface to allow the user to perform calculations
3. Print out a nice result / log to the screen
"""
def add(x, y):
  return x + y

def divide(x, y):
  try:
    return x / y
  except ZeroDivisionError:
    print("You can't divide by zero!")

import math
def area_of_a_circle(radius):
  return math.pi * radius ** 2

def scientific_calculator():
  while True:
    calculation_name = input("Please enter a calculation you would like to perform\n" + \
      "The options are (add/divide/area of a circle) or enter 'quit' to exit the calculator: ")
    if calculation_name == 'add':
      print("Enter two numbers to add together:")
      x = int(input("Enter first number: "))
      y = int(input("Enter second number: "))
      print(add(x, y))
    elif calculation_name == 'divide':
      print("Enter two numbers to divide:")
      x = int(input("Enter numerator: "))
      y = int(input("Enter denominator: "))
      print(divide(x, y))
    elif calculation_name == 'area of a circle':
      print("Enter a radius for the circle to calculate it's area:")
      radius = int(input("Enter a radius: "))
      print(area_of_a_circle(radius))
    elif calculation_name == 'quit':
      break
    else:
      print("Please enter a calculation to perform or 'quit' to exit the calculator!\n")


scientific_calculator()
