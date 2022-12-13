import os

fname = input("Enter the file name : ")
if os.path.isfile(fname):
    print("File Exist")
else:
    print("File Not Exist")