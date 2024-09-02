"""File Concatenation:
Write a Python script that takes multiple text files as input and concatenates their
contents into a single text file."""


file_1 = input('f1')
file_2 = input('f2')
file_3 = input('f3')
with open(file_1, 'r') as f:
    a = f.read()
with open(file_2, 'r') as f:
    b = f.read()
with open(file_3, 'r') as f:
    x = f.read()
with open('file2.txt', 'w') as f:
    f.write(a)
with open('file2.txt', 'a') as f:
    f.write(b)
with open('file2.txt', 'a') as f:
    f.write(x)
with open('file2.txt', 'r') as f:
    content = f.read()
print(content)


