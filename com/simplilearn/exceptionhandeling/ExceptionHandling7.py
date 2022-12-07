


print("I am statement 1")
try:
    print(10/0) # Risky Code
    print("I am statement 2")
except ZeroDivisionError as msg:
    print("I got This Error : ",msg)
    print(10/2)
    print("I am statement 3")
print("I am statement 4")

