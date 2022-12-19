'''
3. Write a Python program to sort a list of tuples using Lambda.
'''

l = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
sorted(l, key=lambda x: x[1])
print(l)