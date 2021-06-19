def prod(myDict):
    p = 1

    for i in myDict:
        p = p * myDict[i]

    return p
dict = {'a': 100, 'b': 200, 'c': 300}
print("product :", prod(dict))