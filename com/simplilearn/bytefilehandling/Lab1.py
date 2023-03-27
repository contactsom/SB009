
print("****** START- IMAGE FILE HANDLING ********")

f=open("simplilearn-logo.jpg",'rb')
f1=open("Simplilearn_NEW_Logo.jpg",'wb')
bytes=f.read()
f1.write(bytes)
print("New Image is getting created")


#print(bytes)