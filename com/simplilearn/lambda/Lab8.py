'''
8. Write a Python program to extract year, month, date and time using Lambda.
'''
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
time = now.time()

print("YEAR - ",year)
print("MONTH - ",month)
print("DAY - ",day)
print("TIME - ",time)