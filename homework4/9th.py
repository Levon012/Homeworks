"""9.Line Segment
You are given four real numbers - the coordinates of two points on a
plane. The first two numbers are the x and y coordinates of the first point,
and the last two numbers are the x and y coordinates of the second point.
Output the length of the line segment bounded by the two points.
Sample Input Sample Output
1 2.2
2.5 -1.5
                 3.9924
0.0 0.0
3.0 4.0
                 5"""

x1 = int(input('number1'))
y1 = int(input('number2'))
x2 = int(input('number3'))
y2 = int(input('number4'))
length = (((x1 - y1)**2 + (x2 - y2)**2)**0.5)
print(length)



