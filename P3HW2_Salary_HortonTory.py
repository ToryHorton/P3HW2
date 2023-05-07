# CTI-110

# P3HW2 - Salary

# Tory Horton

# 4-20-23


 
# user inputs name

employee_name = input("Enter employee's name: ")

# user inputs hours worked

hours_worked = float(input("Enter number of hours worked: ")) # hours worked

pay_rate = float(input("Enter employee's pay rate: ")) # pay rate

print('-------------------------------------')

print(f'{"Employee name:":<20}{employee_name:<10}') # displays employee's name

print()

print('Hours Worked    Pay Rate    Overtime    OverTime Pay    RegHour Pay    Gross Pay')

print('-----------------------------------------------------------------------------------------')

# calculate overtime

overtime_pay_rate = 1.5
overtime = hours_worked - 40 # used to find overtime amount
overtime_rate = overtime * overtime_pay_rate # used to find overtime rate
overtime_pay = pay_rate * overtime_rate # used to find overtime pay

if hours_worked >= 40:
    reg_pay = (hours_worked - overtime) * pay_rate
else:
    reg_pay = (hours_worked * pay_rate)

if hours_worked >= 40:
    gross_pay = overtime_pay + reg_pay # finds the gross pay
else:
    gross_pay = reg_pay


print(f'{hours_worked:.1f}{pay_rate:17.1f}{overtime:11.1f}{overtime_pay:14.2f}{reg_pay:16.2f}{gross_pay:15.2f}')
    
