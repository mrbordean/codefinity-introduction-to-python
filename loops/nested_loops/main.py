produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries = [["Tomatoes", "Lettuce"], ["Milk", "Cheese"]]
for section in groceries:
    for item in section:
        print(f" - {item}")