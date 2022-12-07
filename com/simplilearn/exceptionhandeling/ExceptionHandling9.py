

try:
    x = int(input("Enter the First Number : ")) # 10
    y = int(input("Enter the Second Number : ")) # 0
    print(x/y) # Risky Code
except (ZeroDivisionError,ValueError):
    print("Can not Divide with ZERO OR Please provide Int Value Only ")
