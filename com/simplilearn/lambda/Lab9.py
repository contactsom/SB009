'''
9. Write a Python program to check whether a given string is number or not using Lambda.
'''
num_check = lambda x : x.replace('.','').replace('-','').isdigit()
#num_check('-6.6789')
print(num_check('-6.6789'))
print(num_check('A4567'))