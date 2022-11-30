print("This is for While Loop Example2")
print("****************START-WHILE LOOP Example 2 ****************")

myString = "ABCD"
print(myString)
lengthofString= len(myString) # 4
print(lengthofString)
## While traveling if I found character C in this String then conform to user
k=0
while(k<lengthofString):
    print("Statement 1")
    if(myString[k]=='C'):
        print("Character C Found At : ",k)
        break # Stop the remaining Execution
    k=k+1
print("I AM Done")



print("****************END-WHILE LOOP Example 2 ****************")