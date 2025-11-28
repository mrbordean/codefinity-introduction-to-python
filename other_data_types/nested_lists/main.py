vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
if "carrots" in vegetables and "cucumbers" in vegetables:
    vegetables.sort()
    print("Updated Vegetable Inventory: ",vegetables)
elif "carrots" in vegetables and "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
    vegetables.sort()
    print("Carrots are already in the list.")
    print("Updated Vegetable Inventory: ",vegetables)
elif "carrots" not in vegetables and "cucumbers" in vegetables:    
    vegetables.append("carrots")
    vegetables.sort()
    print("Cucumbers are already in the list.")
    print("Updated Vegetable Inventory: ",vegetables)
else: 
    vegetables.append("cucumbers")
    vegetables.append("carrots")
    vegetables.sort()
    print("Updated Vegetable Inventory: ",vegetables)
