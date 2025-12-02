# # List of products, their prices, and the quantities sold
# products = ["Bread", "Apples", "Oranges", "Bananas"]
# prices = [0.50, 1.20, 2.50, 2.00]  # price per item
# quantities_sold = [150, 200, 100, 50]  # number of items sold

# def calculate_revenue(prices, quantities_sold):
#     revenue_list = []
#     for price, quantity in zip(prices, quantities_sold):
#         revenue_list.append(price * quantity)
#     return revenue_list

# def formatted_output(revenues):
#     sorted_revenues = sorted(revenues)

# revenues = calculate_revenue(prices, quantities_sold)
# revenue_product =  list(zip(products, revenues))
# formatted_output(revenue_product)

# # Example of expected output line (do not remove):
# print(f"{revenue[0]} has total revenue of ${revenue[1]}")

# List of products, their prices, and the quantities sold
# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00] 
quantities_sold = [150, 200, 100, 50] 

def calculate_revenue(prices, quantities_sold):
    revenue_list = []
    for price, quantity in zip(prices, quantities_sold):
        revenue_list.append(price * quantity)
    return revenue_list

def formatted_output(revenue_data):
    # Sắp xếp danh sách
    sorted_revenues = sorted(revenue_data)
    for item in sorted_revenues:
        print(f"{item[0]} has total revenue of ${item[1]}")

# --- PHẦN CHẠY CHƯƠNG TRÌNH ---

revenues = calculate_revenue(prices, quantities_sold)

# ===> SỬA TẠI ĐÂY: Đổi tên biến thành 'revenue_per_product' <===
revenue_per_product = list(zip(products, revenues))

# Gọi hàm in ra kết quả
# Lưu ý: Phải truyền cái list đã gộp (revenue_per_product) vào đây
formatted_output(revenue_per_product)

# Dòng này giữ nguyên theo đề bài yêu cầu (để test)
# Nó sẽ truy cập vào biến revenue_per_product để kiểm tra
print(f"{revenue_per_product[0]} has total revenue of ${revenue_per_product[1]}")