# Inventory Management System

# Problem: Build a small inventory system that stores products, tracks quantities, and calculates stock values.

# Requirements
# - Store products in a dictionary using product IDs as keys.
# - Each product must contain its name, price, quantity, and category.
# - Add new products and update existing stock.
# - Search for products by ID or name.
# - Display products with zero stock and products below a chosen stock threshold.
# - Calculate the total inventory value.
# - Use a set to identify unique product categories.
# - Use loops and comprehensions to generate filtered product lists.

# Example data
# inventory = 
#     {    "P101": 
#          {        "name": "Keyboard",        "price": 800,        "quantity": 5,        "category": "Electronics"    },   
#          "P102":
#          {        "name": "Mouse",        "price": 350,        "quantity": 0,        "category": "Electronics"    }
#     }


# Expected results
# Total inventory value: 4000 $
# Out-of-stock products: Mouse
# Unique categories: Electronics


def Inventory():

    inventory = {
        "P101": {
            "name": "Keyboard",
            "price": 800,
            "quantity": 5,
            "category": "Electronics"
        },
        "P102": {
            "name": "Mouse",
            "price": 350,
            "quantity": 0,
            "category": "Electronics"
        }
   
    }
    
    inventory["P103"]={
            "name":"Monitor",
            "price":2500,
            "quantity":5,
            "category":"Electronics"
        }

    inventory["P101"]["quantity"]=10
    
    return inventory


inv=Inventory()

def calculations(inv):
    total = sum(
        product["price"] * product["quantity"]
        for product in inv.values()
    )

    category = {
        product["category"]
        for product in inv.values()
    }

    products = [
        product["name"]
        for product in inv.values()
    ]

    out_stock = [
        product["name"]
        for product in inv.values()
        if product["quantity"] == 0
    ]

    return total, category, products, out_stock



total, category, products, out_stock=calculations(inv)



def display(inv,total,category,products,out_stock):
    
    for key,value in inv.items():
        if  value["quantity"]==0:
            print("Out of stock:",key, value)
            out_stock=value["name"]

        if value["price"]>=1000:
            print("\nExpensive product:",key, value)
        
    print(f"Total inventory value: {total}$")
    print(f"Out-of-stock products: {out_stock}")
    print(f"Unique categories: Electronics: {category}")


display(inv,total,category,products,out_stock)

def searching (inv):
    product_id=input("\nSearch by ID: ").strip().upper()
    if product_id in inv:
        print(inv[product_id])
    else:
        print("Not Found !")
    

searching(inv)
