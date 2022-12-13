print("This is Example of File Handling ")
print("****** START- FILE HANDLING *********")


f=open("mylist.txt",'a')  # Keep the existing data and write new data on each execution

list=["A\n","B\n","C\n","D\n","E\n"]
f.writelines(list)
f.write("---------------- \n")

print("Data written in to file successfully")
f.close()

print("****** END- FILE HANDLING *********")