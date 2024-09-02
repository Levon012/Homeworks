"""Write a Python program that calculates the Fibonacci sequence up to a given number n
using a while loop. The Fibonacci sequence is a series of numbers where each number
is the sum of the two preceding ones."""


n = int(input('Fibonacci'))
a, b = 1, 2
while a <= n:
    print(a)
    a, b = b, a + b




