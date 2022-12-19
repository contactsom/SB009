'''
21. Write a Python program that sum the length of the names of a given list of names after removing the
names that starts with an lowercase letter. Use lambda function.
'''

sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
filtered = list(filter(lambda x: x[0] == x[0].upper() and x[1:] == x[1:].lower(), sample_names))
l1=len("".join(filtered))
print(l1)