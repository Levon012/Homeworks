"""Write a program that takes a list of numbers as input and counts the number of
even numbers in the list. Use a for loop, an if statement, and the modulus
operator (%) to determine if a number is even or odd."""

numbers = [1, 2, 4, 5, 8]
result = 0
for i in numbers:
    if i % 2 == 0:
        result += 1
print(result)




