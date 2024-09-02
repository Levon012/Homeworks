"""Write a program that takes a list of words and a target word as input. The
program should find and print all words in the list that contain the target word.
Use a for loop, the in operator, and an if statement to check if the target word is
present in each word in the list."""


x = input('target')
y = ['red', 'blue', 'green']
result = []
for i in y:
    if i in x:
        result.append(i)
print(result)



