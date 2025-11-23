# 5. Write a program to enter P, T, R and calculate Compound Interest.

principal = float(input('Enter the initial amount: '))
time = float(input('Enter the time period: '))
rate = float(input('Enter the rate of interest: '))

amount =  principal*(1+rate/100)**time 

compound_interest = amount - principal

print(compound_interest)