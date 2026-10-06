# Problem — Shopping Cart Analyzer
# You have:

# cart = [
#     ("Laptop", 25000),
#     ("Mouse", 500),
#     ("Keyboard", 1200),
#     ("Headset", 1800)
# ]

# Write:

# analyze_cart(cart)

# The function should calculate:

# Total items: 4
# Total price: 28500
# Expensive items: 1

# An item is considered expensive if its price is greater than 5000.

# Then:

# Status: Normal

# If total price is greater than 30000:

# Status: Expensive order


def analyze_cart(cart):
  expensive=0
  total_price=0
  
  for item,price in cart:
    
    total_price+=price
    
    if price>5000:
      expensive+=1

  print(f"Total Items:{len(cart)}")
  print(f"Total price:{total_price}")
  print(f"Expensive Item: {expensive}")
    
  if total_price>30000:
    print("Expensive order")
  else:
    print("Normal")
    
analyze_cart(cart = [
    ("Laptop", 25000),
    ("Mouse", 500),
    ("Keyboard", 1200),
    ("Headset", 1800)
])
