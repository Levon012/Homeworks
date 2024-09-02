"""Write a python function, which create a dictionary
for given number N, where keys are numbers from
1 to N, and values are cubs of that numbers"""


def cubs(n):
    return {i: i ** 3 for i in range(1, n + 1)}
print(cubs(4))






