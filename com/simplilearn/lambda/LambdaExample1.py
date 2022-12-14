def addTwo(a,b):
    c=a+b
    return c

result=addTwo(20,30)
print(result) # 50

print("********** With lambda Function **********")

# lambda argumentList:operation/Expression

lresult=lambda a,b:a+b
print(lresult(20,30))

print("-----------------------------------------")

squreResult=lambda a:a*a
print(squreResult(4))

print("-----------------------------------------")


# To find the biggest number among two

biggest=lambda a,b : a if a>b else b
print(biggest(20,30))
print(biggest(82,83))





