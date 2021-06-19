list = []
num = int(input("Enter the number of elements:"))
for i in range(num):
    n = int(input("Enter the element:"))
    list.append(n)
temp = 0
temp = list[0]
list[0] = list[-1]
list[-1] = temp
print(list)