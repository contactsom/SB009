print("***************START: Function Example ***************")

print("-----------------------------------")


# Defination of function
# Function With argument

def addTwoNumber():
   return 20+30

# Call the function
result= addTwoNumber()
print(result)

print("**************************")

def addTwoNumber1():
   return 20+30

# Call the function
result1= addTwoNumber1()
print(result1+50)


print("**************************")

def getSum(a,b):
   print("First Number Recived in ",a)
   print("Second Number Recived in ", b)
   return a+b
   print("I am done") # Skipped

# Call the function
mySum= getSum(33,22)
print("Sum is : ",mySum)



print("***************END: Function Example ***************")