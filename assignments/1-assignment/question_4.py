# 4. Write a program to enter P, T, R and calculate simple Interest.

principal = int(input('Enter the initial amount: '))
time = int(input('Enter the time period: '))
rate = int(input('enter the rate of interest: '))

simple_interest = principal*time*rate / 100

total_amount  = principal + simple_interest

print(simple_interest)
print(total_amount)