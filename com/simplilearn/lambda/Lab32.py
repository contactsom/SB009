'''
32. Write a Python program to check whether a specified list is sorted or not using lambda.
'''

l = [1, 2, 4, 6, 8, 10, 12, 14, 16, 17]
def sorted_list_check(l) :
    l_sorted = list(sorted(l, key = lambda x : x))
    if l_sorted == l:
        return True
    else:
        return False
l1=sorted_list_check(l)
print(l1)