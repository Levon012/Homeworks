"""4. Write a Python program to change a given string to a new string where the first and last chars
have been exchanged.
Example:
Sample: ‘abcdefgh’
Expected: ‘hbcdefga’"""


num = 'abcdefgh'
print(num[-1:] + num[1:-1] + num[:1])




