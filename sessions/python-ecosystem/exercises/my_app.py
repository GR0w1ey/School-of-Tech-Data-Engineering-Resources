from maths_functions import add_numbers, print_orders, my_orders

def do_my_maths():
  result = add_numbers(12, 34)
  print(f"Yay maths is fun! result = {result}")

# start the application main code

# before
print('--before--')
print_orders(my_orders)

updated_orders = add_order(my_orders, 'Tea')

# after
print('--after--')
print_orders(my_orders)
print_orders(updated_orders)

# save new data over old - deliberately
my_orders = updated_orders

# saved
print('--saved--')
print_orders(my_orders)
print_orders(updated_orders)
