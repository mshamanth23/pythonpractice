#Python Program that Displays, which Letters are in the Two Strings but not in Both
s1=set(input("Enter first string:"))
s2=set(input("Enter second string:"))
a=s1.symmetric_difference(s2)
print("The common letters are:")
for i in a:
    print(i)
