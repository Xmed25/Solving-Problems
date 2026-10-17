# Dictionaries & built-in functions

# Given the sales dictionary:
# sales = {    "Laptop": 5000,    "Mouse": 300,    "Keyboard": 700,    "Monitor": 2500}



# Write code that displays:
# 1. The product with the highest sales.
# 2. The highest sales value.
# 3. The total sales across all products.
# Requirements
# - Use dictionary methods or built-in functions appropriately.
# - Do not hardcode the answer.
# - Your code should still work if the sales values change.

sales = {
    "Laptop": 8000,
    "Mouse": 300,
    "Keyboard": 700,
    "Monitor": 2500
}

highest = float("-inf")
best_product = None

for product, sale in sales.items():
    if sale > highest:
        highest = sale
        best_product = product

print(f"Product with highest sales: {best_product}")
print(f"Highest sales value: {highest}")
print(f"Total sales: {sum(sales.values())}")
