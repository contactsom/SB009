class Lab3:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40
        self.e = 50
        self.f = 60

    def m1(self):
        del self.f

l1 = Lab3()
print("-- Before Delete ---")
print(l1.__dict__)

l1.m1()
print("-- After Delete ---")
print(l1.__dict__)