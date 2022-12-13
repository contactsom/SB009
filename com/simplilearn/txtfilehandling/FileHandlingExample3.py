print("This is Example of File Handling ")
print("****** START- FILE HANDLING *********")

#f=open("abc.txt",'w') # Replace the existing data and write new data on each execution
f=open("abc.txt",'a')  # Keep the existing data and write new data on each execution

f.write("I am 1 Line \n")
f.write("I am 2 Line \n")
f.write("I am 3 Line \n")
f.write("I am 4 Line \n")
f.write("---------------- \n")

print("Data written in to file successfully")
f.close()

print("****** END- FILE HANDLING *********")