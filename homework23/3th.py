"""Vowels in a Word:
○ Create a list of vowels present in a given word."""


word = 'python'
vowel = ['a', 'e', 'i', 'o', 'u']
x = [i for i in word if i in vowel]
print(x)