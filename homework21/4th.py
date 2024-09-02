"""Write a function that takes two lists and returns a new list containing only the common
elements. (without using set)"""


def elements(list_1, list_2):
    result = []
    for i in list_1:
        if i in list_2:
            result.append(i)
    return result
list1 = [7, 8, 9, 10]
list2 = [9, 10, 34, 41]
print(elements(list1, list2))
