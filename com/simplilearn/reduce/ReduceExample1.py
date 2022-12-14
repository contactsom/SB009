from functools import *

myList=[1,2,3,4,5]

result1=reduce(lambda a,b:a+b,myList)
print(result1)


result2=reduce(lambda a,b:a*b,myList)
print(result2)


result3=reduce(lambda a,b:a*b,range(1,100))
print(result3)

result4=reduce(lambda a,b:a+b,range(1,100))
print(result4)