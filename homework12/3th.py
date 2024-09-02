"""Write a function that calculates the average of a list of numbers."""


def num(*numbers):
    sum = 0
    x = len(numbers)
    for i in numbers:
        sum += i
    return sum / x
print(num(5, 7, 9))








