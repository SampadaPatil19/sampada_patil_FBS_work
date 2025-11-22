#  2. Write a program to calculate simple interest based on Principal, Rate and Time (SI = P*R*T/100) 

principal = float(input('Enter the principal amount: '))
rate = float(input('Enter the rate of interest: '))
time = float(input('Enter the time period in years: '))

simple_interest = (principal*rate*time) / 100

print(f'Simple Interest is {simple_interest}.')

print(f'Total Amount at the end will be {principal+simple_interest}')