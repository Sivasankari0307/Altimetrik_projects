# Inheritance example

class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
    
    def get_balance(self):
        return self.balance
    
class SavingsAccount(BankAccount):
    def add_interest(self):
        interest_rate = 0.05  
        interest = self.balance * interest_rate
        self.balance += interest
        print(f"Added interest: {interest}. New balance is {self.balance}.")
class CurrentAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Withdrawal exceeds overdraft limit.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

# Example usage
savings_account = SavingsAccount("123456", "Siva", 1000)
savings_account.deposit(500)
savings_account.withdraw(200)
savings_account.add_interest()  
current_account = CurrentAccount("654321", "Sankari", 2000, 500)
current_account.deposit(1000)