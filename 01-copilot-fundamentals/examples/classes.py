"""
Classes example: How can I define a simple class with methods and instantiate it?
"""

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"


if __name__ == "__main__":
    car = Vehicle("Toyota", "Corolla", 2024)
    print(car.description())
