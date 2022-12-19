'''
30. Write a Python program to check whether a given string contains a capital letter, a lower case letter,
a number and a minimum length using lambda.
'''

valid = lambda x : any(x.isupper() for x in x) and any(x.islower() for x in x) and any(x.isdigit() for x in x)
l1=valid("Aman123Parakash")
print(l1)