class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"💰 ₹{amount} deposited. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("❌ Insufficient funds!")
        else:
            self.balance -= amount
            print(f"💸 ₹{amount} withdrawn. Remaining balance: ₹{self.balance}")

    def check_balance(self):
        print(f"🔍 Account balance for {self.account_holder}: ₹{self.balance}")


# Creating an account
account = BankAccount("John Doe", 5000)
account.check_balance()
account.deposit(2000)
account.withdraw(3000)
account.withdraw(5000)  # Should show insufficient funds
