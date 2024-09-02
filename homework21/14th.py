"""Write a function that capitalizes the first letter of each word in a sentence."""


def capitalize_words(sentence):
    for i in sentence.split():
        return ''.join(sentence[0])
z = 'this is a test'
print(capitalize_words(z))
