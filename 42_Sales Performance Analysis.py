# Problem – Sales Performance Analysis
# Task: Analyze monthly sales for four products.
# sales = np.array([    [1200, 1500, 1800, 2000],  # Laptop    [800, 900, 1100, 1300],    # Keyboard    [500, 700, 650, 900],      # Mouse    [1000, 1200, 1400, 1600]   # Monitor])



# Requirements:
# 1. Calculate total sales for each product.
# 2. Find the best-selling product.
# 3. Calculate the overall sales average.


import numpy as np

products=["Laptop","Keyboard","Mouse","Monitor"]


sales = np.array([
    [1200, 1500, 1800, 2000],  # Laptop
    [800, 900, 1100, 1300],    # Keyboard
    [500, 700, 650, 900],      # Mouse
    [1000, 1200, 1400, 1600]   # Monitor
])

# for n in range(len(products)):
#   print(f"Total Sales for {products[n]} : {sales[n].sum()}")


# another method with enumerate

for i , product in enumerate(products):
  print(f"Total Sales for {product} : {sales[i].sum()}")


best=np.sum(sales,axis=1)
print(f"The best selling product: {products[best.argmax()]}")

print(f"The Average: {np.mean(sales):.2f}")
