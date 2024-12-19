import time

class User:
    def __init__(self, full_name, username, email, password):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.email = email
        self.balance = 0.0
        self.transactions = []
        self.loan = None  # To track loan details

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(("Deposit", amount, time.strftime("%Y-%m-%d %H:%M:%S")))

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        self.transactions.append(("Withdrawal", amount, time.strftime("%Y-%m-%d %H:%M:%S")))
        return True

    def request_loan(self, amount, repayment_time):
        if self.loan:
            print("You already have an active loan. Please repay it first.")
            return False

        # Determine the rate of interest based on repayment time
        if repayment_time <= 1:
            rate_of_interest = 5.0  # 5% for 1 year or less
        elif repayment_time <= 3:
            rate_of_interest = 7.5  # 7.5% for up to 3 years
        else:
            rate_of_interest = 10.0  # 10% for more than 3 years

        # Calculate monthly EMI
        loan_amount = amount
        annual_interest_rate = rate_of_interest / 100
        monthly_interest_rate = annual_interest_rate / 12
        total_months = repayment_time * 12

        emi = (loan_amount * monthly_interest_rate * (1 + monthly_interest_rate)**total_months) / \
              ((1 + monthly_interest_rate)**total_months - 1)

        self.loan = {
            "amount": amount,
            "rate_of_interest": rate_of_interest,
            "repayment_time": repayment_time,
            "approval_date": time.strftime("%Y-%m-%d %H:%M:%S"),
            "monthly_payment": round(emi, 2),
            "status": "Approved"
        }
        self.balance += amount  # Add loan amount to user's balance
        self.transactions.append(("Loan Approved", amount, time.strftime("%Y-%m-%d %H:%M:%S")))
        print(f"Loan of {amount} approved at {rate_of_interest}% interest for {repayment_time} years.")
        print(f"Your monthly payment will be {round(emi, 2)}.")
        return True

    def show_loan_status(self):
        if not self.loan:
            print("No active loan.")
            return
        print("\nLoan Details:")
        print("---------------------")
        print(f"Loan Amount: {self.loan['amount']}")
        print(f"Rate of Interest: {self.loan['rate_of_interest']}%")
        print(f"Repayment Time: {self.loan['repayment_time']} years")
        print(f"Approval Date: {self.loan['approval_date']}")
        print(f"Monthly Payment (EMI): {self.loan['monthly_payment']}")
        print(f"Status: {self.loan['status']}")

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
                print("Username already exists. Please choose a different username.")
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
                full_name = input("Enter a full_name: ")
                username = input("Enter a username: ")
                email = input("Enter an email: ")
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
            print("4. Request Loan")
            print("5. Show Loan Status")
            print("6. Logout")
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
                amount = float(input("Enter loan amount: "))
                repayment_time = int(input("Enter repayment time (in years): "))
                user.request_loan(amount, repayment_time)

            elif choice == '5':
                user.show_loan_status()

            elif choice == '6':
                print("Logging out...")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    banking_system = BankingSystem()
    banking_system.main_menu()
