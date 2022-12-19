'''
36. Write a Python program to find the elements of a given list of strings that contain specific substring using lambda.
'''

l = ['red', 'black', 'white', 'green', 'orange']
def sub_str_search(l, sub_str) :
    return list(filter(lambda x :sub_str in x , l))
l1=sub_str_search(l, 'ack')
print(l1)

l2=sub_str_search(l, 'bmw')
print(l2)