"""8.Create a string made of the first, middle and last character of given string with odd number of
symbols
Example:
Sample = ‘Sevak’
Expected ‘Svk’"""


sample = 'Sevak'
middle = sample[len(sample) // 2]
print(sample[:1] + middle + sample[-1:])