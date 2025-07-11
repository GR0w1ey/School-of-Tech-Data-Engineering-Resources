import json

person_1 = {
  'Name': 'Diego',
  'Type': 'Cat'
}

person_2 = {
  'Name': 'Dora',
  'Type': 'Cat'
}

some_people = [
  person_1,
  person_2
]

print('This is cat 1: ', person_1)
print('This is cat 2: ', person_2)
print('This is everyone: ', some_people)

with open('pets.json', 'w') as pets_file:
    json.dump(some_people, pets_file)
