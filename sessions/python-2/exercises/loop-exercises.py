# 1. Print the numbers 0 to 100 using a for loop.
for i in range(0, 11):
  print(i)

# 2. Print the numbers 0 to 10 using a while loop.
i = 0
while i < 11:
  print(i)
  i += 1

# 3. Print the list of numbers below using a for loop.
numbers_list = [0, 2, 8, 20, 43, 82, 195, 204, 367]
for number in numbers_list:
  print(number)

# 4. Print the message 'Done!' after printing the numbers 0 to 10 with a for loop. Hint: use the for-else construct.
for i in range(0, 11):
  print(i)
else:
  print("Done!")

# 5. Take the below two lists and use a nested for loop to determine if any elements from the first list are in the second. If it finds a match, print out the name of the element.
list1 = ["apple", "banana", "cherry", "durian", "elderberry", "fig"]
list2 = ["avocado", "banana", "coconut", "date", "elderberry", "fig"]

for item_1 in list1:
  for item_2 in list2:
    if item_1 == item_2:
      print(item_1)

"""
 6. Using a while loop, on every iteration generate a random number. If it's a multiple of 5, break from the loop. If it's a multiple of 3, end the current iteration with continue and print a message to show you are skipping. If it's neither, print the number and continue the loop.

When the loop has been broken, print a message indicating that this has happened before the program exits.

Hint:

import random
x = random.randint(1,100)

"""
import random
while True:
  random_int = random.randint(1, 100)
  if random_int % 5 == 0:
    print("The loop has been broken!")
    break
  elif random_int % 3 == 0:
    print("That's a multiple of 3, skip this iteration.")
    continue
  else:
    print(random_int)
