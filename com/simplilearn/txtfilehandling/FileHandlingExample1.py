print("This is Example of File Handling ")
print("****** START- FILE HANDLING *********")

f=open("pogo.txt",'w')

print("File Name",f.name)
print("File Mode",f.mode)
print("Is File Redable : ",f.readable())
print("Is file Writable : ",f.writable())
print("Is File Closed : ",f.closed)

f.close()

print("Is File Closed : ",f.closed)

print("****** END- FILE HANDLING *********")