days_present=int(input("Enter the number of days present: "))
total_working_days=int(input("Enter the number of working days: "))
attendance_percentage=(days_present/total_working_days)*100
if attendance_percentage>=95:
    print("Perfect Attendence Bonus")
else:
    print("No Bonus")     