def add_two_numbers(a, b):
  if isinstance(a, (int, float)) and isinstance(b, (int, float)):
    return a + b
  else:
    message = f"Please only add floats or ints, but was passed '{a}', '{b}'."
    raise TypeError(message)

def price_updater(prices: list[float], increase_rate: float):
  if not isinstance(increase_rate, (int, float)):
    raise TypeError
  elif 0 > increase_rate > 1:
    raise ValueError
  else:
    return list(map(lambda price: (1 + increase_rate) * price, prices))

# result = add_two_numbers(3, 4)
# print(f"3 + 4 = {result}")

# result = add_two_numbers(3.1, 4.6)
# print(f"3.1 + 4.6 = {result}")

# # We expect this to generate an error but the function
# # should reject the strings.
# try:
#   result = add_two_numbers("a", "b")
#   print("It should have blown up with strings and it didn't.")
# except TypeError as expected:
#   print("Expected it to reject strings and it did.")
#   print(expected)

# try:
#   result = add_two_numbers("a", 3)

# except TypeError as expected:
#   print("Exploded with type error as expected.")
#   print(expected)
