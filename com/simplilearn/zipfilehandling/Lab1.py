from zipfile import *

print("****** START- ZIP FILE HANDLING ********")

f=ZipFile("simplilearn.zip",'w',ZIP_DEFLATED)
f.write("abc.txt")
f.write("book.txt")
f.write("employee.txt")
f.write("mylistfile.txt")
f.close()
print("Zip file created successfully")