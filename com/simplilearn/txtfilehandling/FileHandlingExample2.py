print("This is Example of File Handling ")
print("****** START- FILE HANDLING *********")

f=open("book.txt",'w')

f.write("I am 1 Line \n")
f.write("I am 2 Line \n")
f.write("I am 3 Line \n")
f.write("I am 4 Line \n")

print("Data written in to file successfully")
f.close()

print("****** END- FILE HANDLING *********")