import traceback

quotient = 0
try:
  quotient = 5 / 0
except Exception as e:
  print("That's a division by zero the code will crash!")
  traceback.print_exc()
  
fruit_list = ['apple', 'banana', 'tangerine', 'plum']
try:
  print(fruit_list[4])
except Exception as e:
  print("You can't access an element out of bounds!")
  traceback.print_exc()
