class Bank:
    def __init__(self, fname, lname, accid, acctype, pin, balance):
        self.fname = fname
        self.lname = lname
        self.accid = accid
        self.acctype = acctype
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient balance!")
            return self.balance

    def display(self):
        print("\nYour Account Details")
        print(f"First Name: {self.fname}")
        print(f"Last Name: {self.lname}")
        print(f"Account ID: {self.accid}")
        print(f"Account Type: {self.acctype}")
        print(f"Balance: {self.balance:.2f}")

# Collecting user input to create a bank account
print("Welcome to the Bank! Please enter your details to create an account.")

# Taking user inputs
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
accid = int(input("Enter your account ID (numeric only): "))
acctype = input("Enter your account type (e.g., Savings, Current): ")
pin = int(input("Set a 4-digit PIN for your account: "))
balance = float(input("Enter your starting balance: "))

# Creating a Bank object
user_account = Bank(fname, lname, accid, acctype, pin, balance)

# Display account details
user_account.display()

# Perform a deposit
deposit_amount = float(input("\nEnter the amount to deposit: "))
new_balance = user_account.deposit(deposit_amount)
print(f"Your new balance after deposit is: {new_balance:.2f}")

# Perform a withdrawal
withdraw_amount = float(input("\nEnter the amount to withdraw: "))
new_balance = user_account.withdraw(withdraw_amount)
print(f"Your new balance after withdrawal is: {new_balance:.2f}")
