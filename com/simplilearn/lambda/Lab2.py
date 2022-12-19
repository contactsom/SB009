'''
2.Write a Python program to create a function that takes one argument,
 and that argument will be multiplied with an unknown given number.
'''

def multiplier(n) :
    return lambda x:x*n

output = multiplier(5)
print("Quintuple of 3 is: " ,output(3))