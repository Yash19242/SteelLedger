import csv

def show_outstanding():
    try:
        with open("bills.csv", "r") as f:
            reader = list(csv.reader(f))[1:]
            unpaid = [r for r in reader if r[-1].lower() == "unpaid"]
            if not unpaid:
                print("✅ All invoices are paid.")
            else:
                print("\n--- Outstanding Invoices ---")
                for row in unpaid:
                    print(f"{row[0]} | Buyer: {row[4]} | ₹{row[6]} | Vehicle: {row[7]}")
    except FileNotFoundError:
        print("❌ No invoices found.")