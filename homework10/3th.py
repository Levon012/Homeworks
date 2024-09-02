"""Write a Python program that calculates the sum of all even numbers between 1 and 100
using a while loop."""

i = 0
x = []
result = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        x.append(i)
for l in x:
    result += l
print(result)








