'''
4. Write a Python program to sort a list of dictionaries using Lambda.
'''

d = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}
    ]
sorted(d, key = lambda x : x['color'])
print(d)