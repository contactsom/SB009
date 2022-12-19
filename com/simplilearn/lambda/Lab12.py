'''
12. Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
'''

def count_Even_odd(l) :
    even = len(list(filter(lambda x: x % 2 == 0, l)))

    print("Count of Even number in given list is: ", even)
    print("Count of odd number in given list is: ", len(l) - even)

count_Even_odd([1,2,3,4,10,5,6,7,8,9,11,13])