from new import student
obj = student()
a=input("enter your option")
if a == '1':
    regno=input("Enter regno")
    sname=input("Enter name")
    obj.add(regno,sname)
elif a == '2':
    regno=input("enter regno")
    obj.display(regno)
elif a =='3':
    obj.displayall()
elif a == '4':
    regno = input("Enter regno")
    sname = input("Enter name")
    obj.update(regno,sname)
elif a == '5':
    regno=input("enter regno")
    obj.delet(regno)