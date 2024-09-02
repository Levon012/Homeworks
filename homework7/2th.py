"""Count all letters, digits, and special symbols from a given string
Sample Input Sample Output
P@#yn26at^&i5ve       Total counts of chars, digits, and symbols
                      chars = 8
                      digits = 3
                      symbol = 4"""

x = 'P@#yn26at^&i5ve'
chars = 0
digits = 0
symbol = 0
for i in x:
    if i.isupper() or i.islower():
        chars += 1
    elif i.isdigit():
        digits += 1
    else:
        symbol += 1
print(chars)
print(digits)
print(symbol)


 