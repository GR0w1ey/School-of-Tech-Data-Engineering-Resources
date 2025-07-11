# 1. Add a new key-value pair to the below car dictionary for the colour. Print out the colour to verify it worked.
car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year' : 1964,
    'isNew': False
}

car['colour'] = 'blue'
print(car['colour'])

# # 2. Update the value of the model in the car dictionary. Print out the new value to verify it worked.
# car['model'] = 'Focus'
# print(car['model'])

# # 3. Delete the model key-pair from the car dictionary. Print out the entire dictionary to verify it worked.
# del car['model']
# print(car)

# """
# 4. Use the items() function to loop through the dictionary and print each key-value pair like so:

# key: x, value: y
# Hint: for key, value in x.items(): Hint: You will need to cast the values to a string

# """
# for key, value in car.items():
#   print(f"key: {key}, value: {value}")

