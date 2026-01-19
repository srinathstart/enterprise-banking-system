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
    pass




acc = SavingsAccount("Srinath", 1000)

acc.deposit(500)
acc.withdraw(200)

print(acc.get_balance())

