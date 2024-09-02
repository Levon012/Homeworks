"""Create a Python class representing a basic calculator with methods for addition,
subtraction, multiplication, and division."""


# 2 tarberak

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        if self.y == 0:
            raise ValueError('Cannot divide by zero')
        return self.x / self.y

a = Calculator(14, 7)
print(a.addition())
print(a.subtraction())
print(a.multiplication())
print(a.division())





class Calculator:
    def addition(self, x, y):
        return x + y
    def subtraction(self, x, y):
        return x - y
    def multiplication(self, x, y):
        return x * y

    def division(self, x, y):
        if y == 0:
            raise ValueError('Cannot divide by zero')
        return x / y

a = Calculator()
print(a.addition(5, 7))
print(a.subtraction(4, 1))
print(a.multiplication(5, 3))
print(a.division(14, 2))



