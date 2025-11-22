# 3.  Write a program to accept basic salary of n emp. (n should be accepted from user). If basic salary is below 20000 then da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and hra=20%. Based on this calculate the total salary of each emp and also total salary of all emp.


n = int(input('Enter the number of employees: '))
total_salary_of_all_emp = 0

for i in range(1, n+1):
    print(f"For Employee {i}")

    basic_salary = float(input(f'Enter the salary of Employee {i}: '))

    if basic_salary < 20000:
        da = basic_salary * 10 / 100
        ta = basic_salary * 12 / 100
        hra = basic_salary * 15 / 100
    
    else:
        da = basic_salary * 15 / 100
        ta = basic_salary * 18 / 100
        hra = basic_salary * 20 / 100
    
    total_salary = da + ta + hra + basic_salary
    total_salary_of_all_emp += total_salary
    print(f"Salary of {i} employee is {total_salary}") 
    

print(f"Salary of All Employee is {total_salary_of_all_emp}")
