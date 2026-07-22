#calculating profit and loss
revenue=float(input("Enter the revenue: "))
expenses=float(input("Enter the expenses: "))
profit=revenue-expenses 
#comparison operators to check profit or loss
if revenue>expenses:
    print("Profit:",profit)
elif revenue<expenses:
    print("Loss:",abs(profit))
else:
    print("No profit, no loss")
