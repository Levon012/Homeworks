"""Print the multiplication table of 5 using a for loop and f”strings”. The table should be
printed up to 10"""

a = 5
for i in range(1, 11):
    multi = a * i
    print(f'5 * {i} = {multi}')


