"""Write a program to check if two strings are balanced. For example, strings s1 and
s2 are balanced if all the characters in the s1 are present in s2. The character’s
position doesn’t matter.
Sample Input Sample Output
s1 = "Yn"
s2 = "PYnative"
                       True
s1 = "Ynf"
s2 = "PYnative"
                       False"""

s1 = 'Ynf'
s2 = 'PYnative'
result = True
for i in s1:
    if i not in s2:
        result = False
print(result)







