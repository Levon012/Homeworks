"""Find and Replace:
Implement a Python program that reads a text file (input.txt), prompts the user
for a word to find, and another word to replace it with. Replace all occurrences of
the first word with the second word and save the modified text to a new file
(output.txt)."""


# 3 hat tarberak


find_word = input('x')
replace_word = input('y')

with open('input.txt', 'r') as f:
    content = f.read()
new_content = content.replace(find_word, replace_word)
with open('output.txt', 'w') as f:
    f.write(new_content)
print(new_content)



with open('input.txt', 'r') as f:
    content = f.read()
new_content = content.replace('Hello', 'world')
with open('output.txt', 'w') as f:
    f.write(new_content)
print(new_content)


input_file = input('input.txt')
output_file = input('output.txt')
find_word = input('Hello')
replace_word = input('word')
with open(input_file, 'r') as file:
    content = file.read()
new_content = content.replace(find_word, replace_word)
with open(output_file, 'w') as file:
    file.write(new_content)
print(new_content)

