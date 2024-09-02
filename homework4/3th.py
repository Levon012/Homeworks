"""3.Digit Sum
Input a two-digit natural number and output the sum of its digits. You can
assume that the input will be a two-digit number and need not check that
programmatically.
Sample Input Sample Output
15    6
78    15
20    2"""

lion = int(input('number'))
print(lion % 10 + lion // 10)



