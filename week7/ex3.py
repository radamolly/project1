class Calculator:
    @classmethod
    def add(cls,a,b):
        return a + b
    @staticmethod
    def multiply(a,b):
        return a * b

print(Calculator.add(2,3))
print(Calculator.multiply(2,3))