"""Write a function that swaps the values of two tuples."""


# 2 tarberak
def swaper(a1, a2):
    return a2, a1
x = (1, 2, 3)
y = (4, 5, 6)
x, y = swaper(x, y)
print('x:', x)
print('y:', y)


def swaper(a1, a2):
    x = list(a1)
    y = list(a2)
    x[0] = 4
    y[0] = 7
    a = tuple(x)
    b = tuple(y)
    return a, b
n1 = (1, 2, 3)
n2 = (4, 5, 6)
print(swaper(n1, n2))


