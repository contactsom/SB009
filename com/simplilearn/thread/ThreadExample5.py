from threading import *
# 2. Creating the Thread without extending Thread Class

class ThreadExample4:

    def display(self):
        for i in range(1,5):
            print("Child Thread")

t=ThreadExample4() # Object of Class
thread=Thread(target=t.display()) # Thread creation
thread.start() # Start