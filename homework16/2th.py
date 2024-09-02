"""List Element Removal
Write a function that removes an element at a specified index from a list. Handle the
IndexError by raising a custom exception if the index is out of range."""


def list_element(x, index):
    if index not in range(len(x)):
        raise IndexError('Sorry, the index is out of range')
    else:
        del x[index]
    return x
a = [1, 2]
b = 1
print(list_element(a, b))
