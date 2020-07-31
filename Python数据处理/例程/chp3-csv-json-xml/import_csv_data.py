import csv

csvfile = open('../../data/chp3/data-text.csv', 'r')
reader = csv.reader(csvfile)

for row in reader:
    print(row)
