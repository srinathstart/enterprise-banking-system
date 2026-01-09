class Account:
    def __init__(self, account_number, balance):
        print("self is:", self)
        self.account_number = account_number
        self.balance = balance



acc1 = Account(101, 5000)
acc2 = Account(102, 12000)

print(acc1.account_number, acc1.balance)
print(acc2.account_number, acc2.balance)
