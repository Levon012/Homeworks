"""Character Frequency:
○ Given a string, create a dictionary where keys are characters and values are their
frequencies in the string."""


x = 'django'
counter = {i: x.count(i) for i in x}
print(counter)

