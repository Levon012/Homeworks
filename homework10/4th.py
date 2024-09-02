"""Write a Python program that generates a random number between 1 and 100 and asks
the user to guess the number. The program should give hints whether the guessed
number is too high or too low until the correct number is guessed."""

import random
random_num = random.randint(1, 100)
print(random_num)
while True:
    x = int(input())
    if x > random_num:
        print('higher')
    elif x < random_num:
        print('lower')
    else:
        print('correct')
        break






