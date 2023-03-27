# Write a class that meets these requirements.
#
# Name:       BankAccount
#
# Required state:
#    * opening balance, the amount of money in the bank account
#
# Behavior:
#    * get_balance()      # Returns how much is in the bank account
#    * deposit(amount)    # Adds money to the current balance
#    * withdraw(amount)   # Reduces the current balance by amount
#
# Example:
#    account = BankAccount(100)
#
#    print(account.get_balance())  # prints 100
#    account.withdraw(50)
#    print(account.get_balance())  # prints 50
#    account.deposit(120)
#    print(account.get_balance())  # prints 170
#
# There is pseudocode for you to guide you.

class BankAccount:
    def __init__(account, balance):
        account.balance = balance

    def get_balance(account):
        return account.balance

    def withdraw(account, amount):
        account.balance -= amount
        return account.balance

    def deposit(account, amount):
        account.balance += amount
        return account.balance


# Test Example:
account = BankAccount(100)

print(account.get_balance())  # prints 100
account.withdraw(50)
print(account.get_balance())  # prints 50
account.deposit(120)
print(account.get_balance())  # prints 170

# class BankAccount
# method initializer(self, balance)
#     self.balance = balance

# method get_balance(self)
#     returns the balance

# method withdraw(self, amount)
#     reduces the balance by the amount

# method deposit(self, amount)
#     increases the balance by the amount
