
list = []
num = int(input("Enter the number of elements:"))
for i in range(num):
    n = int(input("Enter the element:"))
    list.append(n)
def sort(my_list):
    temp = 0
    for i in range(0, len(my_list)):
        for j in range(i+1, len(my_list)):
            if (my_list[i] <= my_list[j]):
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return(my_list)
print(sort(list))





