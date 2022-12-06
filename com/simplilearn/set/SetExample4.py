print("***************START: Set Mathematical Operations Example ***************")

# UNION
x = {10,20,30,40}
y = {30,40,50,60}

print(x.union(y)) # {40, 10, 50, 20, 60, 30}
print(x|y) # {40, 10, 50, 20, 60, 30}

print("-----------------------------------")

# INTERSECTION
a = {10,20,30,40}
b = {30,40,50,60}
print(a.intersection(b)) # {40, 30}
print(a&b) # {40, 30}

print("-----------------------------------")
# difference
# It return the element present in set m but not in n

m = {10,20,30,40}
n = {30,40,50,60}
print(m.difference(n)) # {10,20}
print(m-n) # {10,20}

print("-----------------------------------")
# symmetric_difference
# It return the elements present in either set1 or set2 but not in both

set1 = {10,20,30,40}
set2 = {30,40,50,60}
print(set1.symmetric_difference(set2)) # {10, 50, 20, 60}
print(set1^set2) # {10, 50, 20, 60}



print("***************END: Set Mathematical Operations Example ***************")