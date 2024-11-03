class Account:
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount}. New balance is ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def view_balance(self):
        print(f"Account Balance for {self.name}: ${self.balance}")


class BankSystem:
    def __init__(self):
        self.accounts = {}  # Dictionary to store accounts by name

    def create_account(self):
        name = input("Enter account name: ")
        if name in self.accounts:
            print("Account with this name already exists.")
            return

        try:
            initial_deposit = float(input("Enter initial deposit: "))
            if initial_deposit < 0:
                print("Initial deposit cannot be negative.")
                return

            new_account = Account(name, initial_deposit)
            self.accounts[name] = new_account
            print(f"Account created successfully for {name} with balance ${initial_deposit}.")
        except ValueError:
            print("Invalid input. Initial deposit should be a number.")

    def deposit_money(self):
        name = input("Enter account name: ")
        if name not in self.accounts:
            print("Account not found.")
            return

        try:
            amount = float(input("Enter amount to deposit: "))
            self.accounts[name].deposit(amount)
        except ValueError:
            print("Invalid input. Deposit amount should be a number.")

    def view_balance(self):
        name = input("Enter account name: ")
        if name in self.accounts:
            self.accounts[name].view_balance()
        else:
            print("Account not found.")

    def run(self):
        while True:
            print("\n1. Create Account\n2. Deposit Money\n3. View Balance\n4. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.deposit_money()
            elif choice == '3':
                self.view_balance()
            elif choice == '4':
                print("Exiting the banking system.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    bank_system = BankSystem()
    bank_system.run()
