"""Write an abstract class with name Employee
Write 2 employee classes by inheriting from abstract Employee
Write function
get_info -> return string with name and position
calculate_salary -> return float with information about employee salary
Calculate salary should be different for 2 classes"""


from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def calculate_salary(self):
        pass

class Doctor(Employee):
    def __init__(self, salary, position):
        self.salary = salary
        self.position = position
    def get_info(self):
        return f"Doctor with position {self.position} and salary {self.salary}"
    def calculate_salary(self):
        return self.salary

class Politician(Employee):
    def __init__(self, salary, position, bonus):
        self.salary = salary
        self.position = position
        self.bonus = bonus
    def get_info(self):
        return f"Politician with position {self.position} and salary {self.salary}"
    def calculate_salary(self):
        return self.salary + self.bonus

emp1 = Doctor(500000, 'surgeon')
emp2 = Politician(700000, 'minister', 50000)
print(emp1.get_info())
print(emp2.get_info())
print(emp2.calculate_salary())

