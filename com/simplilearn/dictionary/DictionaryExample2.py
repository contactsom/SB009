print("***************START: Access the Dictionary Data ***************")

print("-----------------------------------")

# How to create the Dictionary

rollNameDict={100:"Mehdi",101:"Ankit",102:"Akshat"}

print(rollNameDict)
print("-----------------------------------")
print(rollNameDict[100]) # Mehdi
print(rollNameDict[101]) # Ankit
print(rollNameDict[102]) # Akshat

print("-----------------------------------")
#print(rollNameDict[103]) #KeyError: 103

#rollNameDict.has_key(400) # This function exist in Python 2 not in 3

if 103 in rollNameDict:
    print(rollNameDict[103])
else:
    print("103 key Not Exist")




print("***************END: Dictionary Example ***************")