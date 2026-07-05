#Inventory stock checker
current_stock=int(input("Enter the current stock: "))
minimum_stock=int(input("Enter the minimum stock level: "))
minimum_capacity=int(input("Enter the minimum capacity: "))
#using comparison operators to check stock levels
if current_stock<minimum_stock:
    print("Stock is low.")  
elif current_stock>minimum_capacity:
    print("overstocked.")
else:
    print("optimal.")