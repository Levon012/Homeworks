"""Given a list of numbers, write a function to find the sum of all numbers in the list that
can be divided by 7."""


def given_list(numbers):
    result = 0
    for i in numbers:
        if i % 7 == 0:
            result += i
    return result
num = [2, 3, 4, 11, 14, 21]
print(given_list(num))
