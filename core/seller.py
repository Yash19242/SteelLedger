import os
import json

DATA_DIR = "data"

def setup_seller():
    """
    Prompts user to enter their firm (seller) details.
    Saves them to seller.json for reuse.
    """
    print("\n--- Enter Your Firm Details ---")
    seller = {
        "firm_name": input("Firm Name: "),
        "address": input("Address: "),
        "state": input("State (e.g., Maharashtra): "),
        "state_code": input("State Code (e.g., 27): "),
        "gstin": input("GSTIN: "),
        "pan": input("PAN: "),
        "bank_name": input("Bank Name: "),
        "account_no": input("Account Number: "),
        "ifsc": input("IFSC Code: "),
        "branch": input("Bank Branch: ")
    }

    save_seller(seller)
    return seller

def save_seller(data):
    """
    Save seller details to JSON file.
    """
    with open(os.path.join(DATA_DIR, "seller.json"), "w") as f:
        json.dump(data, f, indent=4)

def load_seller():
    """
    Load seller data from seller.json.
    If missing or incomplete, prompts user to re-enter.
    """
    path = os.path.join(DATA_DIR, "seller.json")

    try:
        with open(path, "r") as f:
            data = json.load(f)
            # ✅ Check required fields
            if "state" not in data or "state_code" not in data:
                print("⚠️ Seller file missing state/state_code. Re-enter required fields.")
                return setup_seller()
            return data

    except (FileNotFoundError, json.JSONDecodeError):
        return setup_seller()