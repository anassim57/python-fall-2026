# Get employee information
employee_name = input("Enter employee name: ")
hours_worked = float(input("Enter hours worked this week: "))
hourly_rate = float(input("Enter hourly pay rate ($): "))

# Overtime settings
regular_hours = 40
overtime_rate = 1.5

# Calculate regular and overtime pay
if hours_worked > regular_hours:
    regular_pay = regular_hours * hourly_rate
    overtime_hours = hours_worked - regular_hours
    overtime_pay = overtime_hours * hourly_rate * overtime_rate
else:
    regular_pay = hours_worked * hourly_rate
    overtime_hours = 0
    overtime_pay = 0

# Calculate total gross pay
gross_pay = regular_pay + overtime_pay

# Display payroll report
print("\n========== PAYROLL REPORT ==========")
print("Employee Name:", employee_name)
print("Regular Hours:", min(hours_worked, regular_hours))
print("Overtime Hours:", overtime_hours)
print(f"Hourly Rate: ${hourly_rate:.2f}")
print(f"Regular Pay: ${regular_pay:.2f}")
print(f"Overtime Pay: ${overtime_pay:.2f}")
print(f"Total Gross Pay: ${gross_pay:.2f}")
print("====================================")
