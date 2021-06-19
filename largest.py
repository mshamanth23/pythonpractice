list = []
num = int(input("Enter the number of elements:"))
for i in range(num):
    n = int(input("Enter the element:"))
    list.append(n)
    temp = 0
    for i in range(0, len(list)):
        for j in range(i+1, len(list)):
            if (list[i] >= list[j]):
                temp = list[i]
                list[i] = list[j]
                list[j] = temp

print(f"Largest no is {list[-1]}")