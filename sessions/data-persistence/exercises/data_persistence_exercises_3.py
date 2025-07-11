people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

try:
  file = open("people.txt", 'r+')
  for person in people:
    file.write(person + "\n")
except FileNotFoundError as FNFE:
  print(f"File not found {FNFE}")
finally:
  if file:
    file.close()
    print("File closed.")
  else:
    print("Couldn't find a file to close.")
