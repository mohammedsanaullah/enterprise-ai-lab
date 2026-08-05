"""
Calculator example: How can I build a simple calculator that supports add, subtract, multiply, and divide?
"""

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


if __name__ == "__main__":
    calc = Calculator()
    print("Add: 2 + 3 =", calc.add(2, 3))
    print("Subtract: 5 - 2 =", calc.subtract(5, 2))
    print("Multiply: 4 * 6 =", calc.multiply(4, 6))
    print("Divide: 10 / 2 =", calc.divide(10, 2))
