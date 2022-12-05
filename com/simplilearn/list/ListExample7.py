print("***************START: For Loop List ***************")


print("-----------------------------------")
# (i-x)
# (0-5),(1-5),(2-5),(3-5),(4-5)
#  -5, -4, -3, -2, -1
# [ A,  B,  C,  D,  D ]
#   0,  1,  2,   3,  4

# 5
# Display the elements by index:

l =["A","B","C","D","E"]
x = len(l)
print(x)

for i in range(x):
    print(l[i],"Is Available at posite index : ",i,"And at the negative index ",i-x)


print("***************END: For Loop List ***************")