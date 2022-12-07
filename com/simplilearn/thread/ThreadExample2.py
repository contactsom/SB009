from threading import *
# Creating the Thread without any class
def ankitFriends():
    for i in range(1,5):
        print("** Friends **")


t=Thread(target=ankitFriends) # create thread
t.start() # Starting the thread

for i in range(1,5):
    print("Main Thread: Thank you")