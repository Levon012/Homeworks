"""Dictionary Merge:
○ Given two dictionaries, merge them into a new dictionary, excluding any keys
that start with an underscore."""


dict1 = {'_a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, '_e': 5, 'f': 7}
merged_dict = {k: v for i in [dict1, dict2] for k, v in i.items() if k[0] != '_'}
print(merged_dict)
