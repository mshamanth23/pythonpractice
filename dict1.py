list1=[1,23,4]
list2 = [2,4,6]
d=dict()
for i in range(0,len(list1)):
    for i in range(0,len(list2)):
        d.update({list1[i]:list2[i]})
print(d)
