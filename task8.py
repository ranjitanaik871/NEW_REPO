hours_worked=float(input("Hours worked: "))
overtime_hours=float(input("Overtime hours: "))
standard_working_hours=8
if hours_worked>standard_working_hours:
    overtime_pay=overtime_hours*1.5
    print("Overtime Pay: ",overtime_pay)
else:
    print("No Overtime Pay")