def view_bill(obj):
        """Displays current bill with items and subtotal."""
        print("\n🧾 ===== CURRENT BILL SUMMARY =====")
        obj.total_bill = 0
        for i in range(len(obj.name_items)):
            item_total = obj.cost_items[i] * obj.amount_items[i]
            print(f"{i+1}. {obj.name_items[i]} - ₹{obj.cost_items[i]} x {obj.amount_items[i]} = ₹{item_total}")
            obj.total_bill += item_total
        print(f"💵 Subtotal: ₹{obj.total_bill}")
        print("===================================\n")