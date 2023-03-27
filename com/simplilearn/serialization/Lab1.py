import pickle

# A test object
test_dict = {"Hello": "World!"}
accountNameDict={1001:"Mehdi",1002:"Ankit",1003:"Akshat",1004: "Aditya",1005: "Aditya"}

# Serialization
with open("accountName.pickle", "wb") as writefile:
    pickle.dump(accountNameDict, writefile)
print("Written object in to file accountName.pickle - ", accountNameDict)

# Deserialization
with open("accountName.pickle", "rb") as readfile:
    dict_accountName = pickle.load(readfile)
print("Reconstructed/ read object", dict_accountName)

if accountNameDict == dict_accountName:
    print("Read and Write Object matched ")
else:
    print("Read and Write Object Not matched")