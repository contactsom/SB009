

try:
    print(10/0) # Risky Code
except ZeroDivisionError:
    print("I an in Except ")
finally:
    print("I am finally")
