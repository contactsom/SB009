print("***************START: Exception Handling Example ***************")

# Run Time Error
print("I am statement 1")
try:
    print(10/0) # Risky Code
except ZeroDivisionError:
    print("I am statement 2")


print("***************END: Exception Handling Example ***************")