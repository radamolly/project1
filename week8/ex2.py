class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # protected attribute
        self.__balance = balance  # private attribute

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount

account = BankAccount("1234567890", 1000)
print(account.get_balance())  # Output: 1000
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(2000)  # ไม่สามารถถอนได้เพราะยอดเงินไม่พอ
print(account.get_balance())  # Output: 1500