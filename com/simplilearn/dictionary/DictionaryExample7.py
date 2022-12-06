print("***************START: Function the Dictionary Data ***************")

print("-----------------------------------")

rollNameDict={100:"Mehdi",101:"Ankit",102:"Akshat",103: "Aditya",104: "Bijit"}
print(rollNameDict)
print("---------------len()--------------------")

lengthdict=len(rollNameDict)
print(lengthdict)

print("---------------clear()--------------------")

print("---------------get()--------------------")
dictvalue=rollNameDict.get(103)
print(dictvalue)

print("---------------pop()--------------------")
rollNameDict.pop(104)
print(rollNameDict)

print("---------------popitems()--------------------")
# It remove the arbitrary items (key-Value) from the dictioanry and return the same
rollName={100:"Mehdi",101:"Ankit",102:"Akshat",103: "Aditya",104: "Bijit"}
print(rollName)
items=rollName.popitem()
print(items) #(104, 'Bijit')

print("---------------keys()--------------------")
print(rollName.keys())

print("---------------values()--------------------")
print(rollName.values())


print("---------------items()--------------------")
print(rollName.items())


print("---------------copy()--------------------")
print(rollName)
rollNameNew=rollName.copy()
print(rollNameNew)


print("---------------setdefault()--------------------")
# If the Key exist then it returns the corresponding value
# If not exist , then the entry got added in dictioanry
rollStu={100:"Mehdi",101:"Ankit",102:"Akshat",103: "Aditya",104: "Bijit",105:"Astha",106:"Gowtham"}
print(rollStu)

print(rollStu.setdefault(106,"Gowtham")) # Gowtham
print(rollStu.setdefault(106,"abc")) # Gowtham
print(rollStu)
print(rollStu.setdefault(107,"Elwin")) # Elwin
print(rollStu)


print("***************END: Dictionary Example ***************")

# Elwin