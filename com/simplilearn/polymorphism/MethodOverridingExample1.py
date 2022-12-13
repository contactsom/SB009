class Parent:
    def property(self):
        print("Gold+Land+Cash")

class Child(Parent):
    def property(self):
        print("Gold+Land+Cash+Power")

c=Child()
c.property() # Gold+Land+Cash+Power