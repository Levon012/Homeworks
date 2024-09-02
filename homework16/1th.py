"""String Length Checker
Write a function that checks the length of a string provided by the user. Handle the
TypeError by raising a custom exception if the input is not a string."""


def string_length(word):
    if not type(word) is str:
        raise TypeError('Sorry, the specified type is not a string')
    else:
        return len(word)
print(string_length(7))




