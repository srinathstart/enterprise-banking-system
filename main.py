from accounts.savings_account import SavingsAccount
from accounts.current_account import CurrentAccount

acc1 = SavingsAccount("Srinath", 1000)
acc2 = CurrentAccount("Company", 2000)

accounts = [acc1, acc2]

for acc in accounts:
    acc.withdraw(500)
    print(acc.get_balance())
