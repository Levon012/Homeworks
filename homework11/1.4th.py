"""Write a python function which create dict from 2
lists with the same length"""


def dict_from_list(list1: list, list2: list) -> dict:
    target_dict = {}
    x = 0
    if len(list1) == len(list2):
        for i in list1:
            target_dict[i] = list2[x]
            x += 1
        return target_dict
print(dict_from_list([1, 2, 3, 4], ['Nissan', 'Mers', 'Toyota', 'Lexus']))

