# A man goes for shopping. He buys 5 products. Accept the price of all products and display the total bill after adding 18% GST.

item1 = int(input('Enter the price of 1st item: '))
item2 = int(input('Enter the price of 2nd item: '))
item3 = int(input('Enter the price of 3rd item: '))
item4 = int(input('Enter the price of 4th item: '))
item5 = int(input('Enter the price of 5th item: '))

total_billing = item1 + item2 + item3 + item4 + item5

billing_after_GST = total_billing + (total_billing * 18 / 100)

print(f"final billing of a customer after GST is applied is {billing_after_GST}.")