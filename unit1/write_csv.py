import csv

data = [["name","age","location"],["ring",23,"l1"],["dellas",28,"l2"]]
with open('test44.csv', mode='w', newline='') as file:
    csv_writer=csv.writer(file)
    csv_writer.writerows(data)







