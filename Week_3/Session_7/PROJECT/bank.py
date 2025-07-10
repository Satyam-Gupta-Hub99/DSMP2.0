print("""
📢 Welcome to the Satyam Reserve Bank of India 🏦
"Empowering Your Financial Future 💸"
""")

class Bank:
    """
💼 Bank Management System - Python OOP Project
📆 Created on :- 9 JULY,2025
👨‍💻 Developed by Satyam Kuber Gupta | 💻 Powered by Python | ⚙️ OOP Based 
--------------------------------------------
This is a basic banking system using Object-Oriented Programming in Python.
Users can:
- Create an account
- Deposit and withdraw money
- Set/change PIN
- View balance, account details, and transaction history.
All actions are logged with date and time.
    """
    def __init__(self):
        # 🔧 Initialize user and account details
        self.name = ""
        self.age = ""
        self.phone_number = ""
        self.deposit_amount = 0
        self.pin = ''
        self.balance = 0
        self.withdraw_amount = 0
        self.account_num = ""
        self.transactions = []
        self.menu()

    def menu(self):
        """
        🧭 Displays the main menu and routes the user to selected operations.
        """
        while True:
            print("""
🏦 WELCOME TO SATYAM RESERVE BANK OF INDIA 🏦
✨ How can I assist you today?

1️⃣ Press 1 to Create Account.
2️⃣ Press 2 to Deposit Money
3️⃣ Press 3 to Create PIN
4️⃣ Press 4 to Change PIN
5️⃣ Press 5 to Check Balance
6️⃣ Press 6 to Withdraw Money
7️⃣ Press 7 to View Transaction History
8️⃣ Press 8 to View Account Details
9️⃣ Press 9 to Exit
            """)
            user_input = input("🔢 Select the option: ")
            if user_input == "1":
                self.create_account()
            elif user_input == "2":
                self.deposit_money()
            elif user_input == "3":
                self.create_pin()
            elif user_input == "4":
                self.change_pin()
            elif user_input == "5":
                self.check_balance()
            elif user_input == "6":
                self.withdraw_money()
            elif user_input == "7":
                self.transaction_history()
            elif user_input == "8":
                self.account_details()
            elif user_input == "9":
                print("\n🙏 Thank you for banking with us.")
                print("🔁 Please visit again. Have a great day! 🌞\n")
                break
            else:
                print("❌ Invalid input. Please try again.")

    def create_account(self):
        """
        📝 Collects user details and assigns a random account number.
        """
        user_name = input("Enter the Name: ")
        self.name = user_name
        user_age = int(input("Enter your Age: "))
        self.age = user_age
        while True:
            user_phone_number = input("Enter your Phone Number: ")
            if len(user_phone_number) == 10 and user_phone_number.isdigit():
                self.phone_number = user_phone_number 
                break
            else:
                print("❌ Invalid Number. Please Try Again")
        import random
        account_number = random.randint(10000, 99999)
        print("✅ Your Account is Created Successfully!")
        print("🆔 Your Account Number is:", account_number)
        self.account_num = account_number

    def deposit_money(self):
        """
        💰 Deposits money into the user account after verification.
        """
        while True:
            account_number = input("Enter Account Number: ")
            if account_number == str(self.account_num):
                try:
                    amount_deposit = int(input("Enter Deposit Amount: "))
                    if amount_deposit <= 0:
                        print("⚠️ Amount must be greater than ZERO")
                        continue
                    self.deposit_amount = amount_deposit
                    self.balance += self.deposit_amount
                    timestamp = self.get_current_timestamp()
                    self.transactions.append(f"Deposited: ₹{amount_deposit} on {timestamp}")
                    print("✅ Deposit Successful")
                    break
                except ValueError:
                    print("❌ Invalid Amount. Please Enter Numeric Value")
            else:
                print("❌ Invalid Account Number. Please Try Again")

    def create_pin(self):
        """
        🔐 Creates a new PIN for the user account.
        """
        user_pin = input("Create your PIN: ")
        self.pin = user_pin
        print("✅ PIN created successfully!")

    def change_pin(self):
        """
        🔁 Updates the existing PIN with a new one.
        """
        user_pin = input("Enter your new PIN: ")
        self.pin = user_pin
        print("✅ PIN changed successfully!")

    def check_balance(self):
        """
        💳 Displays the current account balance.
        """
        print("💰 Your current balance is: ₹", self.balance)

    def withdraw_money(self):
        """
        💸 Withdraws money after validating account number, PIN, and balance.
        """
        while True:
            account_number = input("Enter 5 Digit Account Number: ")
            user_pin = input("Enter Your PIN: ")
            if account_number == str(self.account_num) and user_pin == self.pin:
                try:
                    amount = int(input("Enter the amount to withdraw: "))
                    self.withdraw_amount = amount
                    if self.balance >= amount:
                        self.balance -= amount
                        timestamp = self.get_current_timestamp()
                        self.transactions.append(f"Withdrawn: ₹{amount} on {timestamp}")
                        print("✅ Withdrawal successful. Remaining balance: ₹", self.balance)
                        break
                    else:
                        print("❌ Insufficient balance. Your current balance is: ₹", self.balance)
                except ValueError:
                    print("❌ Please enter a valid numeric value")
            else:
                print("❌ Invalid Account Number or PIN")

    def transaction_history(self):
        """
        📜 Displays the list of all past transactions with timestamps.
        """
        account_number = input("Enter Account Number: ")
        if account_number == str(self.account_num):
            print(f"📄 Transaction History of {self.name}")
            if self.transactions:
                for index, entry in enumerate(self.transactions, start=1):
                    print(f"{index}. {entry}")
            else:
                print("📭 No Transactions Found")
        else:
            print("❌ Account number does not match our records.")

    def account_details(self):
        """
        👤 Displays the stored account holder details.
        """
        while True:
            account_number = input("Enter Account Number: ")
            if account_number == str(self.account_num):
                print("🧾 Account Number:", self.account_num)
                print("👤 Name:", self.name)
                print("🎂 Age:", self.age)
                print("📱 Phone Number:", self.phone_number)
                break
            else:
                print("❌ Invalid Account Number.")

    def get_current_timestamp(self):
        """
        🕒 Returns current date and time formatted as DD-MM-YYYY HH:MM:SS
        """
        from datetime import datetime  # 📅 Used for timestamp
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

# 🟢 Start the Bank system
print(Bank.__doc__)  # Show the class-level docstring 📘
obj = Bank()
