print("This is Example of File Handling ")
print("****** START- FILE HANDLING *********")

f=open("data.txt",'r')
#lines= f.readlines()

print(f.read())
print("*******************")
# Because my Current cursor is at last
# to reset my cursor I need to begning again
f.seek(0)
# seek argument can be anything 0 for start .
print(f.read())

#f.close()

print("****** END- FILE HANDLING *********")