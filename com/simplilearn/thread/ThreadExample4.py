from threading import *
# 2. Creating the Thread by extending Thread Class

class ThreadExample4(Thread):

    def run(self):
        for i in range(1,5):
            print("Child Thread")

t=ThreadExample4()
t.start()