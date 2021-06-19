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
print("List2 is",list2)
list3 = list1+list2
print("combined list is",list3)
temp = 0
for k in range(0, len(list3)):
    for l in range(k+1, len(list3)):
        if (list3[k] >= list3[l]):
            temp = list3[k]
            list3[k] = list3[l]
            list3[l] = temp

print("sorted list is",list3)