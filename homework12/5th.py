"""Write a function that calculates the sum of squares of numbers from 1 to n."""


# def sum(number):
#     result = []
#     x = 0
#     for i in (number):
#         result.append(i ** 2)
#         for j in result:
#             x += i
#     return x
# y = 1, 2, 3, 4, 5
# print(sum(y))


# def sum(number):
#     x = 0
#     for i in (number):
#         x += i ** 2
#     return x
# y = 1, 2, 3, 4, 5
# print(sum(y))


# def sum(number):
#     result = []
#     x = 0
#     for i in (number):
#         result.append(i ** 2)
#     for j in result:
#             x += j
#     return x
# y = 1, 2, 3, 4, 5
# print(sum(y))


def sum_squares(number):
    sum_number = 0
    for i in range(1, number + 1):
        sum_number += i ** 2
    return sum_number
print(sum_squares(5))













