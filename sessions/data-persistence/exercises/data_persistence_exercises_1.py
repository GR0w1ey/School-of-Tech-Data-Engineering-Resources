people = ["John", "Sally", "Mark", "Lisa", "Joe", "Barry", "Jane"]

file = open("people.txt", 'w')
for person in people:
  file.write(person + "\n")
    
