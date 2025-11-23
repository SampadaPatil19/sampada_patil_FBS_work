"""
11. Accept age of five people and also per person ticket amount and then calculate total 
amount to ticket to travel for all of them based on following condition : 
a. Children below 12 = 30% discount 
b. Senior citizen (above 59) = 50% discount 
c. Others need to pay full.
"""

total_amount = 0

for i in range(1, 6):
    print(f'For person {i}')

    age = int(input(f'Enter the age of person {i}: '))
    ticket_price = int(input(f'Enter the price of ticket for person {i}: '))

    if age < 12:
        payable_amount  = ticket_price - ticket_price*30/100

    elif age > 59:
        payable_amount  = ticket_price - ticket_price*50/100
    
    else:
        payable_amount  = ticket_price

    total_amount += payable_amount 

print(f'Total amount of tickets for five persons is {total_amount} Rs.')