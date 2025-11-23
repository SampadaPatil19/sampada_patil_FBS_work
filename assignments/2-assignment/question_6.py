# 6. WAP to calculate total salary of employee based on basic, da=10% of basic, ta=12% of basic, hra=15% of basic.

basic_salary = float(input('Enter the basic salary of Employee: '))

ta = basic_salary * 12 / 100
da = basic_salary * 10 / 100
hra = basic_salary * 15 / 100

total_salary = basic_salary + ta + da + hra

print(f'Total salary of the Employee is {total_salary} Rs.')