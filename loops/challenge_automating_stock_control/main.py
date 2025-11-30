# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100
for current_stock in inventory.values():
    while current_stock[0] < current_stock[1]:
        current_stock[0] = current_stock[0] + current_stock[2]

for current_stock in inventory.values():
    if current_stock[0] > discount_threshold:
        current_stock[3] = True

print("Processing started")
for food in inventory:
    print(f"Processing {food}")

print("Processing completed")