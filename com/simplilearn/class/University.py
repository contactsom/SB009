class University:

    def __init__(self):
        self.uni_name="JNU"
        self.uni_zip=56003

    def display(self):
        print("University Name : ", self.uni_name)
        print("University Zip Code : ", self.uni_zip)


u1= University()
u1.display()

# We can access the instance variable also

print(u1.uni_zip)
print(u1.uni_name)


