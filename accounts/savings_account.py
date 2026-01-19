from accounts.account import Account


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
