"""Write a function that checks if two sets are disjoint (have no common elements)."""


def disjoint(set_1, set_2):
    z = set_1 ^ set_2
    return z
x = set('azganunner')
y = set('azgutyun')
print(disjoint(x, y))
