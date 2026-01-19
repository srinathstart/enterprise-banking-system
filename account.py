class Account:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive")
            return

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return

        if amount > self._balance:
            print("Insufficient balance")
            return

        self._balance -= amount


class SavingsAccount(Account):
    
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.withdraw_count = 0

    def withdraw(self, amount):
        if self.withdraw_count >= 3:
            print("Withdrawal limit reached for Savings Account")
            return

        super().withdraw(amount)
        self.withdraw_count += 1

class CurrentAccount(Account):

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return

        # overdraft allowed
        self._balance -= amount




accounts = [
    SavingsAccount("Srinath", 1000),
    CurrentAccount("Company", 2000)
]

for acc in accounts:
    acc.withdraw(500)
    print(acc.get_balance())


