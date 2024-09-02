"""Login System
Write a simple login system where the user enters a username and password. Handle
the KeyError by raising a custom exception if the username is not found in the users
database(dictionary)."""


username = input('username')
password = input('password')
database = {'a': 'lion', 'b': 'system'}
try:
    if database[username] == password:
        print('correct')
except:
    raise KeyError


