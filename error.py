print('hello')
print("hello")
l=[1,2,3]
print(l[2])
try:
    a = int(input("Enter a number"))
    b = int(input("enter second number"))
    print(a + b)

except:
    print("Enter proper number")
else:
    print("No Exceptions were Raised!!")
finally:
    print("This will anyway execute!!")