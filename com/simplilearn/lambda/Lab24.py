'''
24. Write a Python program to sort each sublist of strings in a given list of lists using lambda
'''
l = [
        ['green', 'orange'],
        ['black', 'white'],
        ['white', 'black', 'orange']
    ]
def sort_nestedList(l) :
    l1 = []
    for i in l:
        a = sorted(i, key = lambda x : x[0])
        l1.append(a)
    return l1

l1=sort_nestedList(l)
print(l1)