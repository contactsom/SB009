


print("I am statement 1")
try:
    print(10/0) # Risky Code
    print("I am statement 2")
except ZeroDivisionError:
    print(10/2)
    print("I am statement 3")
print("I am statement 4")

