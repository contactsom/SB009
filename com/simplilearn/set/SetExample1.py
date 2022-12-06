print("***************START: Set Example ***************")

countryName={ "INDIA", "USA", "UK","SRI LANKA","CHINA","ITLY"}
print(countryName)
print(type(countryName)) # <class 'set'>

print("-----------------------------------")

rollNumber = [1,2,3,4,5,6] # list
s=set(rollNumber)
print(s)
print(type(s)) #<class 'set'>

print("-----------------------------------")

mySet=set(range(5))
print(mySet) # {0, 1, 2, 3, 4}
print(type(mySet)) # <class 'set'>

print("-----------------------------------")


#myEmptySet={}
#print(type(myEmptySet)) # <class 'dict'>

myEmptySet=set()
print(type(myEmptySet)) # <class 'set'>



print("***************END: Set Example ***************")