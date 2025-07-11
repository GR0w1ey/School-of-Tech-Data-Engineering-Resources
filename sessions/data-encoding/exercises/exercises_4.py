import csv

with open('even_more_people.csv', 'a', newline='') as people_data:
    csv_writer = csv.writer(people_data, delimiter=',')
    csv_writer.writerow(['Mike', 'Wazowski', 30])
