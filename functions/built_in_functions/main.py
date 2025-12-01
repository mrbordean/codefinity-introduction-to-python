# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []
for name_of_products, price_quantitySold in products.items():
    price_float = float(price_quantitySold[0])
    quantitySold_int = int(price_quantitySold[1])
    sales = price_float * quantitySold_int
    total_sales_list.append(price_float * quantitySold_int)
    print(f"Total sales for {name_of_products}: ${sales}")

total_sum = sum(total_sales_list)
max_sales = max(total_sales_list)
min_sales = min(total_sales_list)

print(f"Total sum of all sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")