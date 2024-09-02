"""5.Duplicates
Write a Python program to remove duplicates from a list.
Sample Input Sample Output
[1, 2, 3, 1]          [1, 2, 3]
[5, 7, 3, 9, 11]      [5, 7, 3, 9, 11]
[25, 1,1, 13]         [25, 1, 13]"""



x = [1, 2, 3, 1]
result = []
for i in x:
    if i not in result:
        result.append(i)
print(result)







