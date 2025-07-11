import copy

def add_numbers(num1, num2):
  return num1 + num2

my_orders = ['Coffee', 'More Coffee']

def print_orders(list_of_orders):
  print(f"orders = {list_of_orders}")

def add_order(old_list, new_name):
  new_list = copy.copy(old_list)
  new_list.append(new_name)
  return new_list
