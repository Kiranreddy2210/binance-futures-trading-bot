def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Invalid side")

def validate_type(order_type):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type")