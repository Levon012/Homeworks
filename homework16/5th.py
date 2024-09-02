"""Type Conversion:
Write a function that prompts the user to enter a number and tries to convert it to an
integer. Handle the TypeError exception by printing a message indicating that the input
is not a valid number. Use a finally block to print "Type conversion process completed."""


def type_conversion(word):
    try:
        return int(word)
    except ValueError:
        raise TypeError('It is not a number.')
    finally:
        return 'Type conversion process completed.'
print(type_conversion('p'))