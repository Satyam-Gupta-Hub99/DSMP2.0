def add_items(obj):
        """Allows user to add multiple items to the bill."""
        while True:
            user_input = input("\n🛒 Do you want to add items? (Y/N): ").capitalize()
            if user_input == 'Y':
                obj.no_items += 1
                name = input("📦 Enter Item Name: ").capitalize()
                obj.name_items.append(name)
                cost = float(input("💰 Enter cost of 1 item (₹): "))
                obj.cost_items.append(cost)
                amount = float(input("🔢 Enter quantity: "))
                obj.amount_items.append(amount)
                print("✅ Item added successfully!\n")
            else:
                print("🛑 Finished adding items.\n")
                break