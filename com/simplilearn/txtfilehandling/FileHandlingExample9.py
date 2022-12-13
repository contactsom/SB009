print("This is Example of File Handling ")
print("****** START- FILE HANDLING *********")

with open("employee.txt",'w') as f:
    f.write("Astha \n")
    f.write("Elvin \n")
    f.write("Abhishek \n")
    f.write("Aditya \n")
    f.write("Bijit \n")
    f.write("Mehedi \n")
    print("Is File is Closed :", f.closed)
print("Is File is Closed :", f.closed)



print("****** END- FILE HANDLING *********")