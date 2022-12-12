class Student:
    def __init__(self, x, y, z):
        self.name = x
        self.roll = y
        self.marks = z

    def display(self):
        print("NAME : ", self.name)
        print("ROll : ", self.roll)
        print("MARKS : ", self.marks)


s1 = Student('Ankit', 101, 80)
s1.display()

s2 = Student('Jaya', 102, 90)
s2.display()