def isEven(a):
    if a%2==0:
        return True
    else:
        return False

#output = isEven(4)
#output = isEven(3)
#print(output)

mylist = [1,3,6,2,8,10]
result= list(filter(isEven,mylist))
print(result)