"""Write a Python program that asks the user to enter a password. Keep asking for the
password until the correct password "secret" is entered. Provide appropriate feedback
to the user."""


word = 'secret'
while True:
    password = input('enter')
    if password == word:
        print('user')
        break
    else:
        print('program')

