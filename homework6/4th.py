"""Write a program that prompts the user to enter a word and checks if it is a
palindrome. A palindrome is a word that reads the same backward as forward.
Use string slicing and an if-else statement to compare the original word with its
reverse."""


palindrome = input('x:')
n = -1
palindrome_check = palindrome[:int(len(palindrome) / 2)]
p = False
for i in palindrome_check:
    if i == palindrome:
        p = True
        n -= 1
if p is True:
    print(p)
else:
    print(f'{p} is not a palindrome')





