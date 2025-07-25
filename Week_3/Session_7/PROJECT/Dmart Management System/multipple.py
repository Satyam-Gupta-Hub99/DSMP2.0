print("""
🛒 Welcome to the DMART Billing System 🧾
"Where Shopping Meets Simplicity!" ✅
=========================================
👨‍💻 Developed By : Satyam Kuber Gupta
📆 Created On     : 25th July, 2025
🏫 Institution     : Government Polytechnic Mumbai
=========================================
""")

class Billing_System:
    """
    📦 DMART Billing System - Python OOP Project
    --------------------------------------------
    🧑‍💻 Developed by: Satyam Kuber Gupta
    📆 Created on   : 25th July, 2025
    🏫 College      : Government Polytechnic Mumbai
    💻 Technology   : Python 3 (Object-Oriented Programming)

    🔍 Project Description:
        This is a terminal-based billing system that allows users to:
        - Add items with quantity & cost
        - View current bill summary
        - Print final bill with 5% tax
        - Exit the system

    🔐 Note:
        This system is for learning/demonstration purposes only.
        It does not connect to any external database or store data permanently.
    """

    def __init__(self):
        """Initialize all billing system lists and launch menu."""
        self.no_items = 0
        self.name_items = []
        self.cost_items = []
        self.amount_items = []
        self.total_bill = 0
        self._menu_()

    def _menu_(self):
        """Display the main menu for user interaction."""
        while True:
            print("""
📋 ========== BILLING MENU ==========
🔘 1. Press 1 to ➕ ADD ITEM
🔘 2. Press 2 to 👁️ VIEW BILL
🔘 3. Press 3 to 🧾 PRINT FINAL RECEIPT
🔘 4. Press 4 to ❌ EXIT
======================================
""")
            user_input = input("👉 Select an Option (1-4): ")
            if user_input == '1':
                self.add_items()
            elif user_input == '2':
                self.view_bill()
            elif user_input == '3':
                self.print_final_bill()
            elif user_input == '4':
                print("\n🙏 Thank you for using the DMART BILLING SYSTEM.")
                print("🔁 Please visit again. Have a great day! 🌞\n")
                break
            else:
                print("❌ Invalid input. Please try again.")

    def add_items(self):
        """Allows user to add multiple items to the bill."""
        while True:
            user_input = input("\n🛒 Do you want to add items? (Y/N): ").capitalize()
            if user_input == 'Y':
                self.no_items += 1
                name = input("📦 Enter Item Name: ").capitalize()
                self.name_items.append(name)
                cost = float(input("💰 Enter cost of 1 item (₹): "))
                self.cost_items.append(cost)
                amount = float(input("🔢 Enter quantity: "))
                self.amount_items.append(amount)
                print("✅ Item added successfully!\n")
            else:
                print("🛑 Finished adding items.\n")
                break

    def view_bill(self):
        """Displays current bill with items and subtotal."""
        print("\n🧾 ===== CURRENT BILL SUMMARY =====")
        self.total_bill = 0
        for i in range(len(self.name_items)):
            item_total = self.cost_items[i] * self.amount_items[i]
            print(f"{i+1}. {self.name_items[i]} - ₹{self.cost_items[i]} x {self.amount_items[i]} = ₹{item_total}")
            self.total_bill += item_total
        print(f"💵 Subtotal: ₹{self.total_bill}")
        print("===================================\n")

    def print_final_bill(self):
        """Calculates tax and prints final total."""
        print("\n🧾 ===== FINAL BILL RECEIPT =====")
        print(f"🕒 Date & Time       : {self.get_current_timestamp()}")
        print(f"🧾 Sub-Total        : ₹{self.total_bill}")
        print(f"🧾 Tax (5%)         : ₹{0.05 * self.total_bill}")
        total_tax = 0.05 * self.total_bill
        total_bill = self.total_bill + total_tax
        print(f"💵 Total Payable    : ₹{total_bill}")
        print("=================================\n")
    def get_current_timestamp(self):
        """
        🕒 Returns current date and time formatted as DD-MM-YYYY HH:MM:SS
        """
        from datetime import datetime  # 📅 Used for timestamp
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        

# Object creation to start system
print(Billing_System.__doc__)
obj = Billing_System()
