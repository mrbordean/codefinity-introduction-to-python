# Inventory dictionary with stock, price, and discount price
inventory = {
    "Bread": [42, 1.20, 0.99],  # "Item": [current stock, regular price, discounted price]
    "Eggs": [225, 2.12, 1.99],  # Eggs should be sold at a discount
    "Apples": [9, 1.50, 1.35]   # Apples need to be restocked
}

for name_of_food, food in inventory.items():
    if food[0] < 30:
        print(f"{name_of_food} need restocking.")
    elif food[0] > 100:
        print(f"{name_of_food} should be sold at the discounted price of {food[2]}.")
    elif 30 < food[0] < 100:
        print(f"{name_of_food} should be sold at the regular price of {food[1]}.")