list = []
num = int(input("Enter the number of elements:"))
for i in range(num):
    n = int(input("Enter the element:"))
    list.append(n)
final_list = []
for num in list:
    if num not in final_list:
       final_list.append(num)
print(final_list)