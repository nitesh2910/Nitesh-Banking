import time

class User:
    def __init__(self,full_name, username, email, password):
        self.full_name = full_name
        self.username = username
        self.email = email
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
        print(f"\nPassbook for {self.full_name} ({self.username}):")
        print("Type        Amount      Date and Time")
        print("----------------------------------")
        for txn in self.transactions:
            print(f"{txn[0]:<12} {txn[1]:<10} {txn[2]}")
        print(f"\nCurrent Balance: {self.balance}\n")

class BankingSystem:
    def __init__(self):
        self.users = {}

    def register_user(self, full_name, username, email, password):
        for user in self.users.values():
            if user.username == username or user.email == email:
                print("Username or email already exists. Please choose a different one.")
                return False
        self.users[username] = User(full_name, username, email, password)
        print("Registration successful!")
        return True

    def login_user(self, login_input, password):
        user = None
        for u in self.users.values():
            if u.username == login_input or u.email == login_input:
                user = u
                break
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
                full_name = input("Enter your full name: ")
                username = input("Enter a username: ")
                email = input("Enter your email: ")
                password = input("Enter a password: ")
                self.register_user(full_name, username, email, password)


            elif choice == '2':
                login_input = input("Enter your username or email: ")
                password = input("Enter your password: ")
                user = self.login_user(login_input, password)
                if user:
                    self.user_menu(user)


            elif choice == '3':
                print("Thank you for using the Banking System. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")

    def user_menu(self, user):
        while True:
            print(f"\nWelcome {user.full_name} ({user.username})")
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
