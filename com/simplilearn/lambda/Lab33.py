'''
33. Write a Python program to extract the nth element from a given list of tuples using lambda.
'''
l = [
        ('Greyson Fulton', 98, 99),
        ('Brady Kent', 97, 96),
        ('Wyatt Knott', 91, 94),
        ('Beau Turnbull', 94, 98)
    ]

def filter_specific(l, n):
    return list(map(lambda x: (x[n]), l))

l1=filter_specific(l, 0)
print(l1)

l2=filter_specific(l, 1)
print(l2)