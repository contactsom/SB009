'''
23. Write a Python program to find the list with maximum and minimum length using lambda.
'''

l = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
def max_length_list(l):
    max_length = max(len(x) for x in l )
    max_list = max(l, key = lambda i: len(i))
    return(max_length, max_list)
x=max_length_list(l)
print(x)


def min_length_list(l):
    min_length = min(len(x) for x in l )
    min_list = min(l, key = lambda i: len(i))
    return(min_length, min_list)
l1=min_length_list(l)
print(l1)