def calculate_tax(seller_state, buyer_state, total):
    if seller_state == buyer_state:
        return round(total * 0.09, 2), round(total * 0.09, 2), 0.0
    return 0.0, 0.0, round(total * 0.18, 2)