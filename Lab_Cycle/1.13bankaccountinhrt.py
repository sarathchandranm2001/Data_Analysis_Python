class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount should be greater than zero.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    
    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: {self.balance}")


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, interest_rate=0.05):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        print(f"Interest applied. New balance is {self.balance}.")


class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance=0.0, overdraft_limit=1000.0):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        available_balance = self.balance + self.overdraft_limit
        if 0 < amount <= available_balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds or overdraw limit exceeded.")



if __name__ == "__main__":
    
    savings = SavingsAccount("SA001", "Sarath", balance=5000.0)
    savings.display_balance()
    savings.deposit(1000.0)
    savings.apply_interest()
    savings.withdraw(2000.0)
    savings.display_balance()
    
    
    current = CurrentAccount("CA001", "Sharrisa", balance=3000.0)
    current.display_balance()
    current.withdraw(4000.0)
    current.withdraw(2000.0)
    current.display_balance()
