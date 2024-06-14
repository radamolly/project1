class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def add_interest(self):
        interest = self._balance * 0.01
        self.deposit(interest)

class CurrentAccount(BankAccount):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self._balance + self.overdraft_limit:
            self._balance -= amount
        else:
            print("Exceeds overdraft limit")

savings = SavingsAccount(1000)
savings.add_interest()
print(savings.get_balance())

current = CurrentAccount(1000, 500)
current.withdraw(1200)
print(current.get_balance())
current.withdraw(800)