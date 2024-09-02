"""Write a Python function to calculate count of each letter in string
Sample Input Sample Output
count_letters(‘abrakadabra’)              {a: 5, b: 2, r: 2, k: 1, d: 1}"""


def letters(calculate):
    count = {}
    for i in calculate:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
print(letters('abrakadabra'))



