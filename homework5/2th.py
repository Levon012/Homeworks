"""2.Largest
Write a Python program to get the largest number from a list.
Sample Input Sample Output
[1, 2, 3, 4]        4
[5, 7, 3, 9, 11]    11
[25, 1,1, 13]       25
[1, 2, 1, 1]        2"""

x = [1, 2, 3, 4]
largest = x[0]
for i in x:
    if i > largest:
        largest = i
print(largest)









