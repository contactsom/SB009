print("************START- For Loop Example ************")

print("--------For Loop Over LIST--------")
myProgLanguage=["JAVA","PYTHON","ANGULAR","REACT",".NET"] # list
             #    0      ,1       ,2        ,3      ,4
print(myProgLanguage)
# 1st Element on Index 0
# 2nd Element on Index 1
# 3rd Element on INdex 2
# 4th Element on Index 3
# 5th Element on Index 4
    ## 5th Element on Index (5-1)
# Kth Element on Index (k-1)

print(myProgLanguage[0]) # JAVA
print(myProgLanguage[1]) # PYTHON
print(myProgLanguage[2]) # ANGULAR
print(myProgLanguage[3]) # REACT
print(myProgLanguage[4]) # .NET

print("**************************")
for var1 in myProgLanguage:
    print(var1)

print("--------For Loop Over Tuple--------")
myProgLanguageTup=("JAVA","PYTHON","ANGULAR","REACT",".NET") # tuple
for var2 in myProgLanguageTup:
    print(var2)


print("--------For Loop Over Set--------")
myProgLanguageSet={"JAVA","PYTHON","ANGULAR","REACT",".NET"} # set
for var3 in myProgLanguageSet:
    print(var3)

print("--------For Loop Over Dictionary--------")

stuRoll={
        1:"Aditya",
        2:"Astha",
        3:"Minitha",
        4:"Akshat"
}

print("------ Get the Key form Dictionary --------")
for var4 in stuRoll:
    print(var4)

print("------ Get the Value form Dictionary --------")

for var5 in stuRoll:
    print(stuRoll[var5])

print("------ Get the KEY and Value form Dictionary --------")

for key , value in stuRoll.items():
    print(key,value)

print("------ Print the Character of String --------")

str1="abcd"
print(str1)

print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
# Length of str1 = 4
# Length of str1 = last Index + 1

print("------------------------")
for s1 in str1:
    print(s1)

print("************END- For Loop Example ************")