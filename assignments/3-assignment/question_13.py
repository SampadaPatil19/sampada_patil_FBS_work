"""
13. Write a program to input electricity unit charges and calculate total electricity bill 
according to the given condition: 
For first 50 units Rs. 0.50/unit 
For next 100 units Rs. 0.75/unit 
For next 100 units Rs. 1.20/unit 
For unit above 250 Rs. 1.50/unit 
An additional surcharge of 20% is added to the bill 
"""

units = int(input('Enter the units of Electricity used: '))

bill = 0

if units <= 50:
    bill = bill * 0.50

elif units <= 150:
    bill = (50*0.50) + (units - 50)*0.75

elif units <= 250:
    bill = (50*0.50) + (100*0.75) + (units - 150)*1.20

else:
    bill = units*1.50

surcharge = bill*20/100

total_bill = bill + surcharge

print(f"Bill before surcharge is {bill} Rs.")
print(f"Additional Surcharge to bill is {surcharge} Rs.")
print(f"Bill After surcharge is {total_bill} Rs.")