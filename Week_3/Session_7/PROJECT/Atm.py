"""
🏧 ATM APPLICATION - Python OOP Project

Created on: 07 July, 2025
Author: Satyam Kuber Gupta

📄 Description:
This is a simple command-line ATM simulation using Object-Oriented Programming in Python.
The user can:
    🔐 Create a PIN and set an initial balance
    🔁 Change their PIN
    💰 Check their balance
    💸 Withdraw money (with PIN verification)
    🚫 Get locked out after 3 incorrect PIN attempts

🎯 Note:
This program does not store data permanently; it's a basic simulation and resets after the program ends.
"""

# 🏧 ATM Application
class Atm:
    """
    🏦 ATM Class
    
    Attributes:
    - pin (str): Stores the user's 4-digit PIN.
    - balance (int): Stores the user's account balance.

    Methods:
    - menu(): Displays ATM options.
    - create_pin(): Creates a new PIN and sets the initial balance.
    - change_pin(): Changes the existing PIN.
    - check_balance(): Displays current balance.
    - withdraw_money(): Allows withdrawal after PIN verification (max 3 attempts).
    """
    
    # 🛠️ Constructor (called automatically when an object is created)
    def __init__(self):
        self.pin = ''         # 🔐 Store user PIN
        self.balance = 0      # 💰 Store user balance
        self.menu()           # 📋 Show menu on initialization

    # 📋 Menu to interact with the ATM
    def menu(self):
        while True:
            user_input = input("""
🌟 WELCOME to ATM 🌟
Hi, How can I help you? 😊

1️⃣ Press 1 to Create PIN 🔐
2️⃣ Press 2 to Change PIN 🔁
3️⃣ Press 3 to Check Balance 💰
4️⃣ Press 4 to Withdraw Money 💸
5️⃣ Press 5 to Exit 🚪
👉 Your choice: """)

            if user_input == "1":
                self.create_pin()
            elif user_input == "2":
                self.change_pin()
            elif user_input == "3":
                self.check_balance()
            elif user_input == "4":
                self.withdraw_money()
            elif user_input == "5":
                print("🙏 Thank you for using the ATM. Goodbye! 👋")
                break  # 🔚 Exit the loop
            else:
                print("⚠️ Invalid input. Please try again.")

    # 🔐 Create a new PIN and set balance
    def create_pin(self):
        user_pin = input("🔧 Create your PIN: ")
        self.pin = user_pin
        try:
            user_balance = int(input("💵 Enter your initial balance: "))
            self.balance = user_balance
            print("✅ PIN created successfully!")
        except ValueError:
            print("❌ Invalid balance input. Please enter a number.")

    # 🔁 Change the existing PIN
    def change_pin(self):
        user_pin = input("🔄 Enter your new PIN: ")
        self.pin = user_pin
        print("✅ New PIN created successfully!")

    # 💼 Check your current balance
    def check_balance(self):
        print(f"💰 Your balance is: ₹{self.balance}")

    # 💸 Withdraw money from the account
    def withdraw_money(self):
        attempts = 3  # 🚫 Limit to 3 attempts
        while attempts > 0:
            user_pin = input("🔐 Enter your PIN: ")
            if user_pin == self.pin:
                try:
                    amount = int(input("💸 Enter amount to withdraw: ₹"))
                    if self.balance >= amount:
                        self.balance -= amount
                        print(f"✅ Withdrawal successful! Remaining balance: ₹{self.balance}")
                        return
                    else:
                        print(f"⚠️ Insufficient balance. Current balance: ₹{self.balance}")
                        return
                except ValueError:
                    print("❌ Invalid input. Please enter a numeric value.")
                    return
            else:
                attempts -= 1
                print(f"❌ Incorrect PIN. You have {attempts} attempt(s) left.")
                if attempts == 0:
                    print("🔒 Access blocked after 3 failed attempts. Please try again after 24 hours.")
                    return

# 🚀 Initialize the ATM system
obj = Atm()
