# Quiz : 4
import os
try:
    print("Try")
    os._exit(0)
except ZeroDivisionError:
    print("Except")
finally:
    print("finally")
