class OperatorOverloadingExample3:
    def __init__(self,name):
        self.name=name



o1=OperatorOverloadingExample3("Abhishek")
o2=OperatorOverloadingExample3("Kumar")

print(o1+o2) #  unsupported operand type(s) for +: