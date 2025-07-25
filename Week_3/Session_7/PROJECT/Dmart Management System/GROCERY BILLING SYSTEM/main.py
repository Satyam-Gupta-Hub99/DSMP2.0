from menu import run_menu  # ✅ import the main menu runner

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
    (docstring as you already wrote)
    """

    def __init__(self):
        """Initialize billing system lists."""
        self.no_items = 0
        self.name_items = []
        self.cost_items = []
        self.amount_items = []
        self.total_bill = 0

# 📌 Object creation to start system
print(Billing_System.__doc__)
obj = Billing_System()

# ✅ Start the menu by passing the object
run_menu(obj)
