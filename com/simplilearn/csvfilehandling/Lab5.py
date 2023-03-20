import csv

with open('teacher.csv', mode='r') as file:
    writer=csv.reader(file)
    for i in writer:
        print(i)