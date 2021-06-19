import re
string ="dhakshdkjad 202001"\
        "202012"\
        "202040"\
    "202030"\
    "Hello"\
    "world"\
    "202017"
pattern = '((2020)([0-2][0-9])|[30]\b)'
result = re.findall(pattern,string)
print(result)
for i in result:
    print(i[0])