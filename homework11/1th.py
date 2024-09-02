"""Write a Python function to find the Max of three numbers.
Sample Input Sample Output
# max_of_three(5, 11, 3)           11"""

def max_of_three(x):
    result = 0
    for i in x:
        if i > result:
            result = i
    return result
y = 5, 11, 3
print(max_of_three(y))


def max_of_three(*args):
    result = 0
    for i in args:
        if i > result:
            result = i
    return result
print(max_of_three(5, 11, 3))


def max_of_three(x: list):
    result = 0
    for i in x:
        if i > result:
            result = i
    return result
print(max_of_three([5, 11, 3]))










