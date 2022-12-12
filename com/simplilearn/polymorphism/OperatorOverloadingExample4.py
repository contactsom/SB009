class OperatorOverloadingExample4:
    def __init__(self,name):
         self.name=name

    def __add__(self, other):
        return self.name+other.name

o1=OperatorOverloadingExample4("Abhishek")
o2=OperatorOverloadingExample4("Kumar")

print(o1+o2) #  AbhishekKumar