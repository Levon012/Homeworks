"""6.Comparison
Input two positive integers, and output a line describing their relation.
Follow the sample format.
Sample Input Sample Output
7 9       7 < 9
11 11     11 = 11
4 -4      4 > -4"""

x = int(input('Pictures'))
y = int(input('Start'))
if x < y:
    print('<')
elif x > y:
    print('>')
else:
    print('=')




