'''
40. Write a Python program to convert string element to integer inside a given tuple using lambda.
'''

t = (
        ('233', 'ABCD', '33'),
        ('1416', 'EFGH', '55'),
        ('2345', 'WERT', '34')
    )
t1=tuple(map(lambda x: (int(x[0]), int(x[2])), t))
print(t1)