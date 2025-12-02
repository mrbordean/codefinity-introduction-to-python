def calculate_total(price, discount=0.05, tax=0.07):
    total_price_default = price * (1 + tax) * (1 - discount)
    return total_price_default

def apply_discount(price, discount=0.05):
    discount_price = price - price * discount
    return discount_price

def apply_tax(price, tax=0.07):
    tax_price = price + price * tax
    return tax_price
    
print(f"Total cost with default discount and tax: ${calculate_total(120)}")
print(f"Total cost with custom discount and tax: ${calculate_total(100, discount=0.10, tax=0.08)}")