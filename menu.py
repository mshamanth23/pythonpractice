import statistics as stat

list = []

n = int(input("Enter the number of observations: "))
for i in range(n):
    num = int(input("Enter the values: "))
    list.append(num)
print(list)
while (True):
    print("MENU \n 1.Mean\n 2.Median\n 3.Mode\n 4.Quit")
    ch = int(input("Enter your choose: "))
    if ch == 1:
        mean1 = stat.mean(list)
        print("The mean of the given observations is: ", mean1)
    elif ch == 2:
        median1 = stat.median(list)
        print("The median of the given data is: ",median1)
    elif ch == 3:
        mode1 = stat.mode(list)
        print("The mode for the given data is: ",mode1)
    elif ch==4:
        break
    else:
        continue
