import csv

csvfile = open('../../data/chp3/data-text.csv', 'r')
reader = csv.DictReader(csvfile)

i = 1
for row in reader:
    print("Id No. {:d}".format(i))
    for key in row:
        print("{} : {}".format(key, row[key]))
    print(' ')
    i += 1
