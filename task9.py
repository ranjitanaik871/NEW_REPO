budget_amount=int(input("Budget amount: "))
allocated_budget=int(input("Allocated budget: "))
department_perfomance_score=int(input("Department performance score: "))

if budget_amount<=allocated_budget and department_perfomance_score>=7:
    print("approval of budget.")
else:
    print("unapproval of budget.")