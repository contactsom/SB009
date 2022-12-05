print("***************START: String Example - Slicing String ***************")
# ABCDEFGH
# A B C D E F G H
# 0 1 2 3 4 5 6 7 : +Ve Index Representation

myString="ABCDEFGH"
print(myString)
# [m:n]
# m - Start Point or FROM
# n - end point : TO
# [FROM:TO]
# n = TO-1

print("[1:5] "+myString[1:5]) # BCDE # from 1 to 5-1=4
print("[0:0] "+myString[0:0]) #
print("[0:8] "+myString[0:8]) # from 0 to 8-1=7
print("[0:80] "+myString[0:80]) # Whole String
print("[0:9] "+myString[0:9]) # ABCDEFGH
print("[:9] "+myString[:9]) # ABCDEFGH
print("[0:] "+myString[0:]) # ABCDEFGH
#print("[80] "+myString[80]) #string index out of range


# ABCDEFGH
#    A   B   C   D   E   F   G   H
#   -8, -7, -6, -5, -4, -3, -2, -1  :- -Ve Index Representation
print("----------------** -Ve Index Slicing -------------------")

print("[-0:-0] "+myString[-0:-0]) # No Output
print("[-1:-0] "+myString[-1:-0]) # No Output
print("[-1:-1] "+myString[-1:-1]) # From = -1 , To -1 : -(1-1) = -0 from -1 tp -0
print("[-1:-4] "+myString[-1:-4]) #

print("[-8:-2] "+myString[-8:-2]) #ABCDEF












print("***************END: String Example - Slicing String ***************")