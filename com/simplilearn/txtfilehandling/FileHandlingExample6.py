print("This is Example of File Handling ")
print("****** START- FILE HANDLING *********")


f=open("book.txt",'r')

data= f.read(5) # First 5 Character
print(data)

print("Data written in to file successfully")
f.close()

print("****** END- FILE HANDLING *********")