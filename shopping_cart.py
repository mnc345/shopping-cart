# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

#print(products)

#1)capture product ids until we're done
#use infinite loop (while loop)

total_price = 0

selected_ids = []

while True:
    selected_id = input("Please select / scan a valid product id 1-20 or select DONE: ")
    if selected_id.upper() == "DONE":
        break
    elif (selected_id == "1") or (selected_id == "2") or (selected_id == "3") or (selected_id == "4") or (selected_id == "5") or (selected_id == "6") or (selected_id == "7") or (selected_id == "8") or (selected_id == "9") or (selected_id == "10") or (selected_id == "11") or (selected_id == "12") or (selected_id == "13") or (selected_id == "14") or (selected_id == "15") or (selected_id == "16") or (selected_id == "17") or (selected_id == "18") or (selected_id == "19") or (selected_id == "20"):
        selected_ids.append(selected_id)
    else:
        print("Invalid product id. Please scan again.")
    #print(selected_id)
#print("WE HAVE REACHED THE END OF THE LOOP")
#print(selected_ids)

#print("WE HAVE REACHED THE END OF THE LOOP")

#2)perform product lookups to determine what the products name and price are

print("\n")
print("*************************")

print("West Side Market")
print("https://www.wmarketnyc.com/")
print("212-807-7771")
print("77 Seventh Avenue, New York, NY 10001")

print("\n")
print("*************************")

from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%a %m/%d/%Y %I:%M:%S %p")
print("\033[1m" + "Checkout At:", dt_string + "\033[0m")


print("\n")
print("*************************")

print("Selected Products:")
for selected_id in selected_ids:
    #print(selected_id)
    # lookup the corresponding product!
    # or maybe display the selected product's name and price
    matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    print("*", matching_product["name"], to_usd(matching_product["price"]))

#print subtotal
#subtotal = str(total_price)

print("Subtotal: " + to_usd(total_price))

subtotal = to_usd(total_price)

sales_tax = 0.0875 * total_price
print("Taxes:", to_usd(sales_tax))

final_total = total_price + sales_tax
print("TOTAL:", to_usd(final_total))

#print total amount

print("\n")
print("*************************")
print("Returns are accepted within 14 days with receipt.")
print("Thank you for shopping at West Side Market!")
print("\n")