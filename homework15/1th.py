"""Dice Rolling Simulator:
○ Develop a simple dice rolling simulator. Generate random numbers between 1 and 6 to
simulate the roll of a six-sided die using the random module."""

# 2 hat tarberak

import random
x = random.randint(1, 6)
print(x)


import random
def roll():
    return random.randint(1, 6)
print(roll())