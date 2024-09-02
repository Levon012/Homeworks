"""Write a function that checks if a sentence is a pangram."""

def text(check):
    sample = 'qwertyuiopasdfghjklzxcvbnm'
    for i in sample:
        if i not in check:
            return False
    return True
sent = 'the five boxing wizards jump quickly.'
print(text(sent))






















