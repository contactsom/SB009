print("***************START: Delete the Dictionary Data ***************")

print("-----------------------------------")

# How to Delete the Dictionary

rollNameDict={100:"Mehdi",101:"Ankit",102:"Akshat",103: "Aditya",104: "Aditya"}

print(rollNameDict)
del rollNameDict[103]
print(rollNameDict)
#del rollNameDict[400]
#print(rollNameDict)

if 400 in rollNameDict:
    del rollNameDict[400]
else:
    print("Can't delete key Not Exist")


print("***************END: Dictionary Example ***************")