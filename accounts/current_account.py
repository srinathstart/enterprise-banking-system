from accounts.account import Account


class CurrentAccount(Account):

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return

        # overdraft allowed
        self._balance -= amount
