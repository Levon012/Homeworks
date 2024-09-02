"""Write a function that returns the nth largest element from a list."""


def largest(*args):
    x = 0
    for i in args:
        if i > x:
            x = i
    return x
print(largest(5, 7, 8, 4, 17))
