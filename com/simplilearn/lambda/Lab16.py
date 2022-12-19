'''
16. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
'''
l = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
l1=list(filter(lambda x : x % 13 == 0 or x % 19 == 0 , l))
print(l1)