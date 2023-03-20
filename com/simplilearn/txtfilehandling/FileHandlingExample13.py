import shutil

print("This is Example of File Handling ")
print("****** START- FILE HANDLING *********")

#Create the duplicate file
shutil.copy("data.txt","New_data.txt")
print("Copy File Created")

print("****** END- FILE HANDLING *********")