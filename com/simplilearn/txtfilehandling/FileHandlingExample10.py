print("This is Example of File Handling ")
print("****** START- FILE HANDLING *********")

f=open("data.txt",'r')
lines= f.readlines()

for line in lines:
    print(line)

f.close()

print("****** END- FILE HANDLING *********")