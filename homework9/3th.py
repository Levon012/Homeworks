"""Print a right-angled triangle pattern using a nested for loop. The pattern should have 5
rows."""

pattern_1 = "*"
pattern_2 = " "
for i in range(1, 6):
    for j in pattern_2:
        print((pattern_1 + pattern_2) * i)



