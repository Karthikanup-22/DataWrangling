
import csv

with open('csvdata.csv',mode='r') as file:
    csv_reader = csv.reader((file))
    for row in csv_reader: 
        print(row)

        