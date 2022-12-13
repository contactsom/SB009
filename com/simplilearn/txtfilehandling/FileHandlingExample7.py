print("This is Example of File Handling ")
print("****** START- FILE HANDLING *********")


f=open("data.txt",'r')

line1= f.readline()
print(line1,end='')

line2= f.readline()
print(line2,end='')

line3= f.readline()
print(line3,end='')

line4= f.readline()
print(line4,end='')

line5= f.readline()
print(line5,end='')

line6= f.readline()
print(line6,end='')

line7= f.readline()
print(line7,end='')

line8= f.readline()
print(line8,end='')

f.close()

print("****** END- FILE HANDLING *********")