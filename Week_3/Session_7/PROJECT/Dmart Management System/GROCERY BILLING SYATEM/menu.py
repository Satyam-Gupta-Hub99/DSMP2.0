def run_menu(obj):
    while True:
        print("""
        🔘 MENU:
        1. Press 1 to ADD ITEM
        2. Press 2 to VIEW BILL
        3. Press 3 to PRINT FINAL RECEIPT
        4. Press 4 to EXIT
        """)
        user_input = input("Select the Option: ")

        if user_input == '1':
            from add_items import add_items
            add_items(obj)
        elif user_input == '2':
            from view_bill import view_bill
            view_bill(obj)
        elif user_input == '3':
            from print_final_bill import print_final_bill
            print_final_bill(obj)
        elif user_input == '4':
            print("\n🙏 Thank you for using DMART BILLING SYSTEM.")
            break
        else:
            print("❌ Invalid input. Please try again.")
