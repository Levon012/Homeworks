"""Filtering Word Lengths:
○ Given a list of words, create a dictionary where keys are words, and values are
their lengths, but only for words with lengths greater than 3."""


a = ['Erevan', 'Moskva', 'Batummi']
word_length = {i: len(i) for i in a if len(i) > 3}
print(word_length)

