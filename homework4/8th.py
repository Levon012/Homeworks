"""8.Three Numbers
Input three integers. Output the word “Sorted” if the numbers are listed in
a non-increasing or non-decreasing order and “Unsorted” otherwise.
Sample Input Sample Output
1 2 3      Sorted
1 3 2      Unsorted
5 0 -4     Sorted
9 9 9      Sorted
9 9 0      Sorted"""


x = int(input('Enter1'))
y = int(input('Enter2'))
z = int(input('Enter3'))

if x > y > z:
    print('Sorted')
elif x < y < z:
    print('Sorted')
elif x == y == z:
    print('Sorted')
else:
    print('Unsorted')
    
    



