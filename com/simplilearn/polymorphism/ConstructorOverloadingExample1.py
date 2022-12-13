class ConstructorOverloadingExample1:
    def __init__(self):
        print("no-Arg Constructor")

    def __init__(self,a):
        print("One-Arg Constructor")

    def __init__(self,a,b):
        print("Two-Arg Constructor")

# Constructor Overloading not possible as it is
obj1=ConstructorOverloadingExample1()