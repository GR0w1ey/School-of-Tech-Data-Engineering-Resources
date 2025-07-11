import csv

# with open("people.csv", 'r') as people_data:
#   csv_reader = csv.DictReader(people_data, delimiter=',')
#   for person_row in csv_reader:
#     print(person_row)

# with open('more_people.csv', 'w', newline='') as people_file:
#     writer = csv.writer(people_file, delimiter=',')

#     writer.writerow(['Diego', 'Cat', 13])
#     writer.writerow(['Dora', 'Cat', 13])

people_field_names = ['first_name', 'last_name', 'age']

with open('more_people.csv', 'w', newline='') as people_file:
    writer = csv.DictWriter(people_file, people_field_names)

    writer.writeheader()
    person = {
      'first_name': 'Diego',
      'last_name': 'Matthews',
      'age': 13,
    }

    writer.writerow(person)
