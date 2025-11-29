prices = [29.99, 45.50, 12.75, 38.20]
discounts = [0.1, 0.2, 0.15, 0.05]

for index in range(len(prices)):    
    prices[index] = prices[index] - prices[index] * discounts[index]
    print(f"Updated price for Item {index + 1}: ${prices[index]:.2f}")
    