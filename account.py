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



acc = Account("Srinath", 1000)

acc.deposit(500)
print(acc.get_balance())

acc.deposit(-200)
print(acc.get_balance())

acc.withdraw(300)
print(acc.get_balance())

acc.withdraw(1000)
acc.withdraw(-50)

print(acc.get_balance())
