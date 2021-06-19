#1. Write a Python function that takes 3 numbers and returns the largest number

def max(num):
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    num3 = int(input("Enter third number:"))
    largest = 0
    if (num1 > num2) and (num1 > num3):
        largest = num1
    elif (num2 > num1) and (num2 > num3):
        largest = num2
    else:
        largest = num3

    print("The largest number is", largest)
max(3)

#2. Write a Python function that takes a number as input and returns the cube of that number
def cube(num):
    return num * num * num
number = int(input("Enter the number:"))
cub = cube(number)
print("The cube of number is", cub)

#3. Write a Python function that takes a list and returns that list, sorted in descending order

list = []
num = int(input("Enter the number of elements:"))
for i in range(num):
    n = int(input("Enter the element:"))
    list.append(n)
def sort(my_list):
    temp = 0
    for i in range(0, len(my_list)):
        for j in range(i+1, len(my_list)):
            if (my_list[i] <= my_list[j]):
                temp = my_list[i]
                my_list[i] = my_list[j]
                my_list[j] = temp
    return(my_list)
print(sort(list))

#4. Write a Python function that takes a string and prints the number of vowels and consonants in it
#i/p - Python
#o/p - Python has 1 vowel and 5 consonants
def vowel(str):
    v = ['a', 'e', 'i', 'o', 'u']
    vowels = 0
    consonant = 0
    for i in str.lower():
        if i in v:
            vowels += 1
        else:
            consonant += 1
    print("Total Number of Vowels in this String = ", vowels)
    print("Total Number of Consonants in this String = ", consonant)
str =  input("Please Enter Your  String : ")

print(vowel(str))

#5. Write a Python function that takes a string and splits it into words and returns a list
#i/p - Welcome to the world of Python
#o/p - ['Welcome', 'to', 'the', 'world', 'of', 'Python']

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

