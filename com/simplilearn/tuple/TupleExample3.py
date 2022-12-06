print("***************START: Tuple Index Representation Example ***************")

#    0,  1, 2, 3, 4, 5
t = (10,20,30,40,50,60)
#   -6, -5,-4,-3,-2,-1

print(t[0]) # 10
print(t[2]) # 30
print(t[-3]) # 40
#print(t[100]) # tuple index out of range
print("-----------------------------------")

print(t[2:5]) # 30, 40 ,50
print(t[2:500]) # 30, 40 ,50 , 60
print(t[2:]) # (30, 40, 50, 60)
print(t[:4]) # (10, 20, 30, 40)

print("-----------------------------------")

print(t[-2:5]) # (50,)
print(t[-2:-5]) # ()
print(t[-5:-2]) # (20, 30, 40)

print("-----------------------------------")
print(t[::2]) # (10, 30, 50)


print("***************END: Tuple Index Representation Example ***************")