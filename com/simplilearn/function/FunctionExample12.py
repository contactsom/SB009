print("***************START: Function Example ***************")

def calculator(a,b):
  sum = a+b
  sub = a-b
  mul = a*b
  div = a/b
  return sum,sub,mul,div


sumResult,subResult,mulResult,divResult=calculator(30,20)
print(sumResult,subResult,mulResult,divResult)

print("***************END: Function Example ***************")