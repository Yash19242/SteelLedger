import os, json

DATA_DIR = "data"

def select_or_add_buyer():
    path = os.path.join(DATA_DIR, "buyers.json")
    buyers = json.load(open(path)) if os.path.exists(path) else {}

    # Show existing buyers if available
    if buyers:
        print("\n--- Select Buyer ---")
        for i, name in enumerate(buyers, 1):
            print(f"{i}. {name}")
        print(f"{len(buyers)+1}. New Buyer")
        choice = int(input("Choice: "))
        if 1 <= choice <= len(buyers):
            selected_buyer = buyers[list(buyers)[choice - 1]]

            if "state" not in selected_buyer or "state_code" not in selected_buyer:
                print("⚠️ Buyer missing state details. Please re-enter.")
                del buyers[list(buyers)[choice - 1]]
                with open(path, "w") as f:
                    json.dump(buyers, f, indent=4)
                return select_or_add_buyer()

            return selected_buyer

    # Add new buyer with full validation
    print("\n--- Enter New Buyer Details ---")
    buyer = {
        "name": input("Buyer Name: "),
        "address": input("Address: "),
        "state": input("State (e.g., Gujarat): "),
        "state_code": input("State Code (e.g., 24): "),
        "gstin": input("GSTIN: ")
    }

    # Save new buyer
    buyers[buyer["name"]] = buyer
    with open(path, "w") as f:
        json.dump(buyers, f, indent=4)
    return buyer