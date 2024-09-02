"""Random Password Generator:
○ Write a function that generates a random password for the user. Allow the user to
specify the length and complexity of the password (include letters, numbers, and
symbols).
Ogtvel random u string module-neric (string.ascii_letters,
string.digits, string.punctuation, )"""


import random
import string
def generate_password(num, letters = False, digits = False, symbols = False):
    generate_pass = ''
    if letters:
        generate_pass += string.ascii_letters
    if digits:
        generate_pass += string.digits
    if symbols:
        generate_pass += string.punctuation
    password = ''
    if letters:
        password += random.choice(string.ascii_letters)
    if digits:
        password += random.choice(string.digits)
    if symbols:
        password += random.choice(string.punctuation)
    x = len(password)
    while x < num:
        password += random.choice(generate_pass)
        x += 1
        return password
print(generate_password(int(input('pl')), True, True, True))
