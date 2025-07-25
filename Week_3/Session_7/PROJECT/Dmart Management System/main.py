class Billing_System:
    def __init__(self):
        self.no_items = 0
        self.name_items = ""
        self.cost_items = 0
        self.amount_items = 0
        self.total_bill = 0
        self._menu_()
    def _menu_(self):
        while True:
            print("""
                  1. Press 1 to ADD ITEM
                  2. Press 2 to VIEW BILL
                  3. Press 3 to PRINT FINAL RECEIPT
                  4. Press 4 to EXIT
                  """)
            user_input = input("Select the Opton: ")
            if user_input == '1':
                self.add_items()
            elif user_input == '2':
                self.view_bill()
            elif user_input == '3':
                self.print_final_bill()
            elif user_input == '4':
                 print("\n🙏 Thank you for DMART BILLING SYSTEM with us.")
                 print("🔁 Please visit again. Have a great day! 🌞\n")
                 exit()
            else:   
                 print("❌ Invalid input. Please try again.")
    def add_items(self):
            while True:
                user_input = input("Do You Want to Add Items to Bill (Y/N): ").capitalize()
                if user_input == 'Y':
                     self.no_items += 1
                     name = input("Enter Item Name: ")
                     self.name_items = name
                     cost = int(input("Enter the cost of 1 Product: "))
                     self.cost_items = cost
                     amount = int(input("Enter the Quantity: "))
                     self.amount_items = amount
                     bill = cost * amount
                     self.total_bill = self.total_bill + bill
                     print(self.total_bill)
                else:
                     break
    def view_bill(self):
            print("Current Bill:")
            print(f"{self.name_items} X {self.amount_items} = {self.total_bill}")
    def  print_final_bill(self):
            print("Total:",self.total_bill)
            print("Tax(5%)",self.total_bill/5)
            print("Total Bill",(self.total_bill/5)+self.total_bill)
obj = Billing_System()