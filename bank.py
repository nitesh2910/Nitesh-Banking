import time

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("Deposit", amount, time.strftime("%Y-%m-%d %H:%M:%S")))

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        self.transactions.append(("Withdrawal", amount, time.strftime("%Y-%m-%d %H:%M:%S")))
        return True

    def show_passbook(self):
        print(f"\nPassbook for {self.username}:")
        print("Type        Amount      Date and Time")
        print("----------------------------------")
        for txn in self.transactions:
            print(f"{txn[0]:<12} {txn[1]:<10} {txn[2]}")
        print(f"\nCurrent Balance: {self.balance}\n")

class BankingSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose a different username.")
            return False
        self.users[username] = User(username, password)
        print("Registration successful!")
        return True

    def login_user(self, username, password):
        user = self.users.get(username)
        if not user or user.password != password:
            print("Invalid username or password.")
            return None
        print("Login successful!")
        return user

    def main_menu(self):
        while True:
            print("\nWelcome to the Banking System")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter a username: ")
                password = input("Enter a password: ")
                self.register_user(username, password)

            elif choice == '2':
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                user = self.login_user(username, password)
                if user:
                    self.user_menu(user)

            elif choice == '3':
                print("Thank you for using the Banking System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

    def user_menu(self, user):
        while True:
            print(f"\nWelcome {user.username}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Show Passbook")
            print("4. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                user.deposit(amount)
                print(f"Deposited {amount} successfully.")

            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                if user.withdraw(amount):
                    print(f"Withdrew {amount} successfully.")
                else:
                    print("Insufficient balance.")

            elif choice == '3':
                user.show_passbook()

            elif choice == '4':
                print("Logging out...")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    banking_system = BankingSystem()
    banking_system.main_menu()
