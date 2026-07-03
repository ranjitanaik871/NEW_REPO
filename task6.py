product_price=float(input("Enter the product price: "))
discount_percentage=float(input("Enter the discount percentage: %"))

discount_amount=(product_price*discount_percentage)/100

tax_percentage=float(input("\nEnter the tax percentage: %"))
tax_amount=(product_price*tax_percentage)/100
final_price=product_price-discount_amount+tax_amount
print("\nDiscount Amount: ",discount_amount)
print("Tax Amount: ",tax_amount)
print("Final Price: ",final_price)
