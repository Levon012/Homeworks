"""Write a Python program to add two given lists using map and
lambda.(map-y kara function-ic heto mekic avel hajordakanutyun
ynduni, orinak erku list)
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9]"""


list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
result = list(map(lambda x, y: x + y, list_1, list_2))
print(result)


