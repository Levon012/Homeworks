"""3.Smallest
Write a Python program to get the smallest number from a list.
Sample Input Sample Output
[1, 2, 3, 4]        1
[5, 7, 3, 9, 11]    3
[25, 1,1, 13]       1
[1, 2, 1, 1]        1"""

x = [1, 2, 3, 4]
small = x[0]
for i in x:
    if i < small:
        small = i
print(small)



