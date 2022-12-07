from threading import *

print(current_thread().getName()) # MainThread
current_thread().setName("ABC")
print(current_thread().getName()) # ABC