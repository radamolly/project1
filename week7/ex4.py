class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b=1):
        return a * b
    
    def subtract(self, a, b):
        return a - b

    def sum(self, *args):
        return sum(args)

    def calculate(self, **kwargs):
        if 'add' in kwargs:
            return self.add(kwargs['a'], kwargs['b'])
        elif 'multiply' in kwargs:
            return self.multiply(kwargs['a'], kwargs.get('b', 1))
        else:
            return self.subtract(kwargs['a'], kwargs['b'])

calc = Calculator()
print(calc.add(3, 5))  # Output: 8
print(calc.multiply(3))  # Output: 3
print(calc.multiply(3, 5))  # Output: 15
print(calc.subtract(8,6))
print(calc.sum(1, 2, 3, 4, 5))  # Output: 15
print(calc.calculate(add=True, a=3, b=5))  # Output: 8
print(calc.calculate(multiply=True, a=3))  # Output: 3