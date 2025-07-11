people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

try:
  with open("people.txt", 'r+') as file_object:
    for person in people:
      file_object.write(person + "\n")
except FileNotFoundError as FNFE:
  print(f"File not found {FNFE}")
