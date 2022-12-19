'''
10. Write a Python program to find intersection of two given arrays using Lambda.
'''

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [2,4,6,8,11,12]
intersection = list(filter(lambda x : x in l1 , l2))
print(intersection)