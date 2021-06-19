from new import student
import re

def check(name):
    if not re.match('^[A-za_z]*$',sname):
        return False
    return True
while True:
    print(f"""Enter a Number from the following Menu:
                1. Add a New Student Record
                2. Edit a Student Record
                3. Delete a Student Record
                4. Show Details of a Student
                5. Show All Students Details
                Enter 6 to Quit
                """)
    obj=student()
    choice=input("Enter ur choice")
    if choice == '1':
        regno=input("enter the register number")
        while True:
            sname=input("Enter name")
            if not check(sname):
                print("Name must contains alphabets")
            else:
                break
        if obj.add(regno,sname):
            print("error")
        else:
            print("added")
    elif choice == '2':
        regno = input("Enter Register Number: ")
        print("The Current Details are: ")
        obj.display(regno)
        sname = input("Enter Student Name to be Updated: ")
        if obj.update(regno,sname):
            print("successfully")
        else:
            print("error")

    elif choice == '3':

        regno = input("Enter Register Number: ")
        print("The Details of this Register Number is as follows:")
        obj.display(regno)
        confirm = input("Are you sure you want to Delete this record? (Y/N): ")
        if confirm.lower() == 'y':
            if obj.delet(regno):
                print("Deleted Successfully !!")
            else:
                print("Some Errors Have Happened!!")
    elif choice == '4':
        regno = input("Enter Register Number: ")
        obj.display(regno)
    elif choice == '5':
        obj.displayall()
    elif choice == '6':
        break
    else:
        print("Enter a Valid Choice")