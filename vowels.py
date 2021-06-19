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






