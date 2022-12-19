'''
15. Write a Python program to find the second lowest grade of any student(s) from the given names and grades of each
student using lists and lambda.
'''

l = [
        ['S ROY', 1.0],
        ['B BOSE', 3.0],
        ['N KAR', 2.0],
        ['C DUTTA', 1.0],
        ['G GHOSH', 1.0]
    ]
la=list(sorted(l, key = lambda x : x[1], reverse= True))[1]
print(la)
