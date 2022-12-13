class ConstructorOverloadingExample1:
    def __init__(self,*a):
        print("Constructor with 0 | 1 | 2 |3 No of Argument")



# Constructor Overloading not possible as it is
obj1=ConstructorOverloadingExample1()
obj2=ConstructorOverloadingExample1(10)
obj3=ConstructorOverloadingExample1(10,20)