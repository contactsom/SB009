import csv

reader= csv.DictReader(open("books.csv"))
for raw in reader:
    print(raw)