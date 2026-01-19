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


        
acc = Account("Srinath", 1000)

acc.deposit(500)
print(acc.get_balance())

acc.deposit(-200)
print(acc.get_balance())
