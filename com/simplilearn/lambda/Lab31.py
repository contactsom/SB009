'''
31. Write a Python program to filter the height and width of students, which are stored in a dictionary using lambda.
'''

d = {
        'Cierra Vega': (6.2, 70),
        'Alden Cantrell': (5.9, 65),
        'Kierra Gentry': (6.0, 68),
        'Pierre Cox': (5.8, 6)
    }

d1=dict(filter( lambda x: (x[1][0], x[1][1]) > (6, 70), d.items()))
print(d1)