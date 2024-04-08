def dis(price, discount):
    final_price = price - (price * (discount / 100))
    return round(final_price, 2)
