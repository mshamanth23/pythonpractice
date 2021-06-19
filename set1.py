#Python Program to Count the Number of Vowels Present in a String using Sets
str  = "GeeksforGeeks"
vowel = set("aeiouAEIOU")
count = 0
for i in str:
    if i in vowel:
        count = count + 1
print("No. of vowels :", count)


