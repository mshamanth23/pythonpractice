f = open('classtest.csv',encoding='utf-8')
print(f.readline())
given = f.read().split('\n')
f.close()
given.pop()
result = dict()
print(given)
print(len(given))
for i in given:
    slist = i.split(',')
    result[slist[0]] = slist[2]
    print(slist)
#email = input("Enter the email address: ")
#print(f"The score of{email} is {result[email]}")

#name = input("enter the name:")
#if name == name.lower():
#print(f"The score of{name} is {result[name]}")
#for i in result:
   # if int(result[i]) == 10:
    #    print(i)

for i in result:
    if int(result[i])  % 2 != 0:
        print(i)

x = open('hello.txt','r+')
g_str=str(input("Enter a string:"))
x.write(g_str)
print(x.read())
x.close()

