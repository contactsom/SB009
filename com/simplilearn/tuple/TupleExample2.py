print("***************START: Tuple Example ***************")
# Empty Tuple
t=()
print(type(t)) #<class 'tuple'>
print(t) #()

print("-----------------------------------")
# Tuple Function

myData=[10,20,30] # list
t=tuple(myData)
print(t)
print(type(t)) # <class 'tuple'>

print("-----------------------------------")

t1=tuple(range(10,20,2))
print(t1)
print(type(t1)) # <class 'tuple'>

print("***************END: Tuple Example ***************")