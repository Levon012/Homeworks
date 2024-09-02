"""You are given three lists, list1, list2, and list3. Your task is to implement a
programm that takes these lists and prints the following:
The set of elements that are common to all three lists.
The set of elements that are present in at least two of the three lists, but not in all
three.
The set of elements that are unique to each list (present in only one list)."""

list1 = {'1', '2', '3', '4'}
list2 = {'1', '2', '7', '9'}
list3 = {'1', '4', '8', '12'}
a = (list1 & list2 & list3)
b = ((list1 & list2) - list3) ^ ((list1 & list3) - list2) ^ ((list2 & list3) - list1)
c = (list1 - list2 - list3) | (list2 - list1 - list3) | (list3 - list1 - list2)
print(a)
print(b)
print(c)



