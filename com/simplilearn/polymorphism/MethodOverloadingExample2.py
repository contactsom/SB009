class MethodOverloadingExample2:


    def m1(self,a=None,b=None,c=None):

        if (a!=None and b!=None and c!=None):
            print("Sum of three numbers are - ", a+b+c)
        elif(a!=None and b!=None):
            print("Sum of three numbers are - ", a + b)
        elif (a != None):
            print("Only One number  - ", a )
        else:
            print("Please provide the two Numbers")


t=MethodOverloadingExample2()
t.m1()         # Please provide the two Numbers
t.m1(10)       # Only One number  -  10
t.m1(10,20)    # Sum of three numbers are -  30
t.m1(10,20,30) # Sum of three numbers are -  60