"""Write a python function, which add a new value
with given key in dict."""


def add_dict(x, key, value):
    x[key] = value
    return x
my_dict = {'q': 7, 'w': 8}
new_key = 'e'
new_value = 9
print(add_dict(my_dict, new_key, new_value))



