from datetime import datetime
import csv
import os

from core.seller import load_seller
from core.buyers import select_or_add_buyer
from core.products import get_products
from core.tax import calculate_tax
from core.pdf_export import export_pdf
from core.report import show_outstanding

BILLS_CSV = "bills.csv"

def get_invoice_number():
    """
    Count lines in bills.csv to return next invoice number
    """
    try:
        with open(BILLS_CSV, "r") as f:
            return len(list(csv.reader(f)))  # includes header
    except FileNotFoundError:
        return 1

def create_invoice():
    """
    Collects all data, calculates totals, saves invoice to CSV and generates PDF.
    """
    seller = load_seller()
    buyer = select_or_add_buyer()
    invoice_number = get_invoice_number()

    fiscal = f"{datetime.now().year}-{str(datetime.now().year + 1)[-2:]}"
    invoice_id = f"MSH/{invoice_number:03}/{fiscal}"
    date = datetime.now().strftime("%d-%m-%Y")

    products = get_products()
    total = sum(p["amount"] for p in products)

    # Tax calculation based on state match
    cgst, sgst, igst = calculate_tax(seller["state"], buyer["state"], total)
    round_off = round(round(total + cgst + sgst + igst) - (total + cgst + sgst + igst), 2)
    grand_total = round(total + cgst + sgst + igst + round_off)

    transport = input("Enter Transport / Vehicle No / E-Way Bill: ")

    # ✅ Ask payment status with validation
    while True:
        paid_status = input("Is this invoice paid? (yes/no): ").strip().lower()
        if paid_status in ["yes", "no"]:
            break
        print("❌ Invalid input. Please type yes or no.")

    paid = "Paid" if paid_status == "yes" else "Unpaid"

    # Save invoice to CSV
    with open(BILLS_CSV, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            invoice_id, date, seller["firm_name"], seller["gstin"],
            buyer["name"], buyer["gstin"],
            grand_total, transport, paid
        ])

    # Export PDF
    export_pdf(invoice_id, date, seller, buyer, products, transport,
               total, cgst, sgst, igst, round_off, grand_total)

def main_menu():
    """
    Show user menu and route to appropriate feature
    """
    while True:
        print("\n===== SteelLedger Menu =====")
        print("1. Create New Invoice")
        print("2. Show Outstanding Invoices")
        print("3. Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            create_invoice()
        elif choice == "2":
            show_outstanding()
        elif choice == "3":
            print("👋 Exiting SteelLedger. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()