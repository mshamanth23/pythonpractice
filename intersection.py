list1 = []
num1 = int(input("Enter the number of elements of list1:"))
for i in range(num1):
    n1 = int(input("Enter the element:"))
    list1.append(n1)
print("List1 is",list1)
list2 = []
num2 = int(input("Enter the number of elements of list2:"))
for j in range(num2):
    n2 = int(input("Enter the element:"))
    list2.append(n2)
list3=[]
print("List2 is",list2)
list4=[]
for k in range (0,len(list1)):
    for l in range(0,len(list2)):
        if(list1[k] == list2[l]):
            list3.append(list1[k])
print(list3)
