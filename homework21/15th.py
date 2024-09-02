"""Write a function that performs the following tasks:
Accepts a list and an index as input.
Attempts to access the element at the given index in the list.
Handles both IndexError
Uses a finally block to print "Task completed" regardless of whether an exception
occurred or not."""


def function(sequence, index):
    try:
        return sequence[index]
    except IndexError:
        print('List index out of range')
    finally:
        print('Task completed')

x = [1, 4, 7]
y = 3
print(function(x, y))
