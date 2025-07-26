from datetime import datetime  # Move this import to the top (only once)
from view_bill import view_bill

def get_current_timestamp():
    """
    🕒 Returns current date and time formatted as DD-MM-YYYY HH:MM:SS
    """
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def print_final_bill(obj):
    """Calculates tax and prints final total."""
    print("\n🧾 ===== FINAL BILL RECEIPT =====")
    view_bill(obj)
    print(f"🕒 Date & Time       : {get_current_timestamp()}")
    print(f"🧾 Sub-Total        : ₹{obj.total_bill}")
    tax = 0.05 * obj.total_bill
    print(f"🧾 Tax (5%)         : ₹{tax}")
    total_bill = obj.total_bill + tax
    print(f"💵 Total Payable    : ₹{total_bill}")
    print("=================================\n")