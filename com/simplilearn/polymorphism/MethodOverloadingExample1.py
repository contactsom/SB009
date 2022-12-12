class MethodOverloadingExample1:
    def m1(self):
        print("No Argument Method") # 1

    def m1(self,a):
        print("One Argument Method") # 2

    def m1(self, a,b):
        print("Two Argument Method") # 3


t=MethodOverloadingExample1()
# t.m1()
# t.m1(10)
t.m1(10,20) # In this Example it consider the last method