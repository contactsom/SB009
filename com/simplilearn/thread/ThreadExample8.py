from threading import *

def test():
    print("Child Thread")

t=Thread(target=test())
t.start()

print("Main Thread identification number : ",current_thread().ident) #4335125888
print("Child Thread identification number : ",t.ident) #6151761920