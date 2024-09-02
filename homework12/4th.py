"""Write a function that finds the index of a given element in a list. If the element is not
present, return -1."""


def index(list, element):
    for i in range(len(list)):
        if list[i] == element:
            return i
    return -1
a = [1, 2, 3, 4, 5, 7]
b = 3
print(index(a, b))



