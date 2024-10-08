"""Write a function that calculates the square root of a number using the math module"""


import math
def square_root(number):
    if number < 0:
        raise ValueError('Cannot calculate the square root of a negative number')
    return math.sqrt(number)
result = square_root(16)
print(result)

