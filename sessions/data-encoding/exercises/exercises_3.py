import csv

people_field_names = ['first_name', 'last_name', 'age']
with open('even_more_people.csv', 'w', newline='') as people_data:
    csv_writer = csv.writer(people_data, delimiter=',')

    csv_writer.writerow(['Joe', 'Bloggs', 40])
    csv_writer.writerow(['Jane', 'Smith', 50])
