'''
17. Write a Python program to find palindromes in a given list of strings using Lambda.
'''

l = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
l1=list(filter(lambda x : x if x == x[::-1] else '', l))
print(l1)