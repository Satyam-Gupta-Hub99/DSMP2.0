def calculate_total_bill(obj):
    obj.total_bill = 0
    for i in range(len(obj.name_items)):
        item_total = obj.cost_items[i] * obj.amount_items[i]
        obj.total_bill += item_total

def view_bill(obj):
    """Displays current bill with items and subtotal."""
    print("\n🧾 ===== CURRENT BILL SUMMARY =====")
    calculate_total_bill(obj)
    for i in range(len(obj.name_items)):
        item_total = obj.cost_items[i] * obj.amount_items[i]
        print(f"{i+1}. {obj.name_items[i]} - ₹{obj.cost_items[i]} x {obj.amount_items[i]} = ₹{item_total}")
    print(f"💵 Subtotal: ₹{obj.total_bill}")
    print("===================================\n")
