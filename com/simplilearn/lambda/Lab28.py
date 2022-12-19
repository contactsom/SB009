'''
28. Write a Python program to extract specified size of strings from a give list of string values using lambda.
'''

l = ['Python', 'list', 'exercises', 'practice', 'solution']

def ret_str_specifiedLen(list_input, length):
    return list(filter(lambda x: x if len(x) == length else '', list_input))
l1=ret_str_specifiedLen(l, 8)
print(l1)