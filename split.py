def split(string):
    a = []
    b = ""
    for i in string:
        if i == ' ':
            a.append(b)
            b=""
        else:
            b= b + i
    a.append(b)
    return a
str = input("Please Enter Your  String : ")
print(split(str))