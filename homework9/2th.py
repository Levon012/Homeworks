"""Print a square pattern using a nested for loop. The pattern should have 5 rows and 5
columns."""

pattern_1 = "*"
pattern_2 = " "
x = 0
y = 5
for i in range(x, y):
    for j in pattern_2:
        print((pattern_1 + pattern_2) * y)
        

