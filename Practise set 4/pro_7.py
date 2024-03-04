# 7) Accept the string from the user; display the count of vowels and consonants.
a = str.lower(input("Enter Any String :"))
print("---------------------------------")
len = len(a)
vowel = 0
const = 0
space = 0

for i in range(len):
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u' :
        vowel += 1
    elif a[i]==' ':
        space += 1
    else:
        const+=1
print("Vowel in given string :", vowel)
print("Constant in given string :", const)
print("Space in given string :", space)
