"""Write a Python program to find intersection of two given arrays using
Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]"""


x1 = [1, 2, 3, 5, 7, 8, 9, 10]
x2 = [1, 2, 4, 8, 9]
intersection = list(filter(lambda x: x in x2, x1))
print(intersection)


