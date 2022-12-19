'''
11. Write a Python program to rearrange positive and negative numbers in a given array using Lambda
'''

l = [-1, 2, -3, 5, 7, 8, 9, -10]
sortedList=sorted(l,key = lambda x: x > 0,reverse=True)
print(sortedList)