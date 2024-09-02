"""3. Write a Python program to remove the n-th index character from a nonempty string.
Example:
Sample string: ‘abcdefgh’
n - 3
Expected result: abcefgh"""



lion = 'abcdefgh'
n = 3
print(lion[:n] + lion[n + 1:])





