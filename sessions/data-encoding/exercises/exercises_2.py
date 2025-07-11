import csv

with open('ford_escort.csv', 'r', newline='') as car_data:
    csv_reader = csv.DictReader(car_data, delimiter=',')
    for car_row in csv_reader:
        print(car_row)
