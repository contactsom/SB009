# List of Employee Salary [50 Employee]
# 1. Find the top max Salary                 = Output count is less or Equal = Filter
# 2. TO increase all the EMp sal by 20 %     = Output count is Same = Map

myList = [1,2,3,4,5,6,7] # 7
def doubleMe(a):
    return a*2

list1 = list(map(doubleMe,myList))
print(list1)

print("-------------------------------")

l = [1,2,3,4,5,6,7]
l1 = list(map(lambda x:2*x,l))
print(l1)