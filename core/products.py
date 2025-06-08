def get_products():
    items = []
    count = int(input("\nNumber of products: "))
    for i in range(count):
        print(f"\nProduct {i+1}")
        item = input("Description: ")
        hsn = input("HSN Code: ")
        qty = float(input("Quantity: "))
        rate = float(input("Rate per unit: "))
        discount = float(input("Discount: "))
        amount = qty * rate - discount
        items.append({"item": item, "hsn": hsn, "qty": qty,
                      "rate": rate, "discount": discount, "amount": amount})
    return items