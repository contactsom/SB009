'''
19. Write a Python program to find all anagrams of a string in a given list of strings using lambda.
'''
from collections import Counter

l = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
l1=list(filter(lambda x: x if Counter("abcd") == Counter(x) else '', l))
print(l1)