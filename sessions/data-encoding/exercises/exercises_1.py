import csv

with open('ford_escort.csv', 'r', newline='') as car_data:
    csv_reader = csv.reader(car_data, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        print(row)
