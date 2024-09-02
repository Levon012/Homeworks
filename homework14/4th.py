"""File Splitting:
Develop a Python Function that reads a large text file (input.txt) and splits it
into smaller files, each containing a specified number of lines. Function paramis
ter the number of lines per file. Generate multiple output files (output1.txt,
output2.txt, etc.)."""


def split_file(file_split, number):
    with open(file_split, 'r') as file:
        content = file.read()
        new_content = content.split('\n')
        n = 0
        num = 1
        i = 1
        n_rows = 0
        small_file = 'file_' + str(num) + '.txt'
        if len(new_content) % number != 0:
            n_rows = len(new_content) // number + 1
        while i <= n_rows:
            with open(small_file, 'w') as f:
                f.write('\n'.join(new_content[n:n + number]))
                n += number
                i += 1
                num += 1
                small_file = 'file_' + str(num) + '.txt'
print(split_file('file1.txt', 5))



















