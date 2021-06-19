#Python Program that Displays, which Letters are in the First String but not in the  Second
s1=set(input("Enter first string:"))
s2=set(input("Enter second string:"))
a=s1.difference(s2)
print("The letters are:")
for i in a:
    print(i)