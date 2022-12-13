import csv

with open('books.csv','rt') as f:
    data=csv.reader(f)
    for row in data:
        print(row)