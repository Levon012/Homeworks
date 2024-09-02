"""Create a class called BankAccount to represent a basic bank account. The class should
have the following attributes:
1. owner: The name of the account owner.
2. balance: The current balance of the account.
Implement the following methods:
1. __init__(self, owner, balance): Initializes the BankAccount object with the
owner's name and initial balance. Ensure that the balance is a non-negative
integer.
2. get_balance(self): Returns the current balance of the account.
3. deposit(self, amount): Adds the specified amount to the account balance.
Ensure that the amount is a positive integer.
4. withdraw(self, amount): Subtracts the specified amount from the account
balance. Ensure that the amount is a positive integer and does not exceed the
current balance.
Additionally, use @property and @attribute.setter to encapsulate the balance
attribute and enforce validation rules."""


class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            raise ValueError('Balance must be a non_negative integer.')

    def get_balance(self):
        return self.balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError('Deposit amount must be a positive integer.')
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            ValueError('Withdrawal amount must be a positive integer.')
account = BankAccount('Levon', 1000)
account.deposit(700)
account.withdraw(200)
print(account.get_balance())




