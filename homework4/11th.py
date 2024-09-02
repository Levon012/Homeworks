"""11.Rounding - 2
Given a real number, round it to the nearest whole.
Sample Input Sample Output
0.3          0
1.2398       1
1.5          2
67.567       68"""


x = float(input('num'))
if x - int(x) >= 0.5:
    print(int(x) + 1)
else:
    print(int(x))









    