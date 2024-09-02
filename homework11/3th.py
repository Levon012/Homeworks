"""Write a Python function to calculate the factorial of a number (a non-negative
integer). The function accepts the number as an argument.
Sample Input Sample Output
factorial(5)          120"""


def fact(number):
    i = 1
    calculate = 1
    while i <= number:
        calculate *= i
        i += 1
    return calculate
y = 5
print(fact(y))



