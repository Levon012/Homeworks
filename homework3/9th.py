"""9. Append new string in the middle of a given (even number of characters) string
Example:
Sample = ‘python’
new_string = ‘new’
Expected ‘pytnewhon"""


sample = 'python'
new_string = 'new'
x = len(sample) // 2
print(sample[:x] + new_string + sample[x:])



