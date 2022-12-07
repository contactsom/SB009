

try:
    x = int(input("Enter the First Number : ")) # 10
    y = int(input("Enter the Second Number : ")) # 0
    print(x/y) # Risky Code
except ZeroDivisionError as msg:
    print("Can not Divide with ZERO ")
except ValueError:
    print("PLease provide Int Value Only ")