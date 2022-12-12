class Student:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name


s= Student()
s.setName("Akshat")
print(s.getName())