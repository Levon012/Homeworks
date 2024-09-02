"""Write a function that finds the key with the maximum value in a dictionary."""


def maximum_value(find):
    result = 0
    for k, v in find.items():
        if v > result:
            result = v
    return result
k_v = {'a': 17, 'b': 21, 'c': 7}
print(maximum_value(k_v))