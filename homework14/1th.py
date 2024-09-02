"""Character Count:
Write a Python script that reads a text file (input.txt) and counts the
occurrences of each character (including spaces and punctuation). Output the
character frequency to another text file (output.txt)."""


with open('input.txt', 'r') as f:
    content = f.read()
    word = {}
    for i in content:
        if i in word:
            word[i] += 1
        else:
            word[i] = 1
with open('output.txt', 'w') as f:
    f.write(str(word))
with open('output.txt', 'r') as f:
    x = f.read()
print(x)



















