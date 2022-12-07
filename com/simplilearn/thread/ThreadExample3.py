from threading import *
# Creating the Thread without any class
def display():
    for i in range(1,5):
        print("** Child Thread **")

t=Thread(target=display) # create thread
t.start() # Starting the thread

for i in range(1,5):
    print("Main Thread: Thank you")