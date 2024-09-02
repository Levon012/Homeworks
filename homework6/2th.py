"""Write a program that takes a string as input and counts the number of vowels (a,
e, i, o, u) in the string. Use a for loop, an if statement, and the in operator to
check if a character is a vowel."""

name = input('Hello world')
vowel = ['a', 'e', 'i', 'o', 'u']
result = 0
for i in vowel:
    if i in name:
        result += 1
print(result)











