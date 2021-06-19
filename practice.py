n=int(input("Enter the number"))
while n>0:
    if n==1:
        print(1)
    else:
         print(n*fact(n-1))