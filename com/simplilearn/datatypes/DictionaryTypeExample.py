print("This is the Dictionary Data Type Example ")

print("****** START ********")

# It hold the data in Key and Value Pair
# Where as :
# KEY   : Always Unique
# Value : May Duplicate also

employeeDetails={
        "adity@simplilearn.com":"Aditya",
        "bijit@simplilearn.com":"Bijit",
        "biji@simplilearn.com": "Bijit"
}  # Dictionary of <String>:<String> type

print(type(employeeDetails)) #<class 'dict'>
print(employeeDetails) # {'adity@simplilearn.com': 'Aditya', 'bijit@simplilearn.com': 'Bijit', 'biji@simplilearn.com': 'Bijit'}

print("------------------------")

stuRoll={
        101:"Aditya Kumar",
        102:"Astha Chourey",
        103: "Bijit Das"
}# Dictionary of <int>:<String> type
print(type(stuRoll))
print(stuRoll)

print("****** END ********")