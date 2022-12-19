'''
14. Write a Python program to add two given lists using map and lambda.
'''

l1 = [3,5,7]
l2 = [1,3,5]
add=list(map(lambda x,y : x + y, l1, l2))
print(add)
