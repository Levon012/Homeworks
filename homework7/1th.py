"""Arrange string characters such that lowercase letters should come first
Sample Input Sample Output
PyNaTive       yaivePNT"""


text = 'PyNaTive'
x = []
y = []
for i in text:
    if i in text.lower():
        x.append(i)
    elif i in text.upper():
        y.append(i)
print(''.join(x + y))















