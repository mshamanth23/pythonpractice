#Python Program that Displays, which Letters are Present in Both the Strings
s1=set(input("Enter first string:"))
s2=set(input("Enter second string:"))
a=s1.intersection(s2)
print("The common letters are:")
for i in a:
    print(i)