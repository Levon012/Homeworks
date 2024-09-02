"""Create a Python class representing a car with methods for accelerating and braking."""


class Car:
    def __init__(self, make, model, speed = 0):
        self.make = make
        self.model = model
        self.speed = speed
    def accelerate(self, amount):
        self.speed += amount
        return f'The car accelerates at a speed of {amount} km/h.'
    def brake(self, amount):
        self.speed -= amount
        if amount < 0:
            raise ValueError('Sorry, not possible')
        return f'The car decelerates at a speed of {amount} km/h.'

my_car = Car('Lexus', 'IS250')
print(my_car.accelerate(50))
print(my_car.brake(15))


