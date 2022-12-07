import os

try:
    print("This is try block")
    os._exit(0) # Forcely termenating your code
except NameError:
    print("I an in Except ")
finally:
    print("I am finally I always execute")
