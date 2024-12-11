"""
Create a function named calculate_discount(price, discount_percent) that calculates the final
 price after applying a discount. The function should take the original price (price) and the
 discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply
 the discount; otherwise, return the original price.
Using the calculate_discount function, prompt the user to enter the original price of an item
and the discount percentage. Print the final price after applying the discount, or if no discount
 was applied, print the original price.
"""

def calculate_discount(price, discount_percentage):
    if discount_percentage >= 20:
        final_price = price * (100 - discount_percentage) / 100
        return final_price
    return price

try:
    initial_price = float(input("Enter the price: "))
    discount = float(input("Enter the percentage discount: "))

    result = calculate_discount(initial_price, discount)
    if result < initial_price:
        print(f"The price after discount is {result}")
    else:
        print(f" There was no discount on that, the final price is {result}")
except ValueError:
    print("Enter valid values for price and discount")



