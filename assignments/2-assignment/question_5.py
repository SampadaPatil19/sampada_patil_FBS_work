# 5. WAP to calculate selling price of book based on cost price and discount.

cost_price = int(input('Enter the cost price of Book: '))
discount = int(input('How much discount on this Book? '))

discount_price = cost_price*discount/100

selling_price = cost_price - discount_price

print(f'Selling Price of the Book is {selling_price} Rs.')