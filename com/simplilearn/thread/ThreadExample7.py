from threading import *

print("Before name Change")
print(current_thread().name) # MainThread
current_thread().setName("SIMPLILEARN")

print("After name Change")
print(current_thread().name) # ABC

