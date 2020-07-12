# Create a bank account class that has two attributes
#   * owner
#   * balance
# And Two methods
#   * deposit
#   * withdraw
# Additional requirements
#   * withdrawals may not exceed the available balance


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"

    def deposit(self, amt):
        if amt > 0:
            self.balance += amt
            print(f"${amt} was deposited into {self.owner} account")
        else:
            print("Unable to deposit")

    def withdraw(self, amt):
        if amt < 0:
            print("Unable to withdraw")
        else:
            if self.balance >= amt:
                self.balance -= amt
                print(
                    f"${amt} was withdrawned. There is ${self.balance} left in the account.")
            else:
                print("Insufficient funds. Unable to withdraw.")


acct1 = Account('Jose', 100)
print(acct1)
acct1.deposit(100)
acct1.withdraw(200)
print(acct1)
print()
