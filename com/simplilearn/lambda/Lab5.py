'''
5. Write a Python program to filter a list of even/odd integers using Lambda.
'''

lint = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x : x % 2 == 0 , lint))
print(even)

odd = list(filter(lambda x : x % 2 != 0 , lint))
print(odd)