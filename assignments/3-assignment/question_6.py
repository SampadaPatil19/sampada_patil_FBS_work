# 6. Write a program to calculate profit or loss.


cost_price = float(input("Enter Cost Price (CP): "))
selling_price = float(input("Enter Selling Price (SP): "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"You made a PROFIT of Rs. {profit}")

elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"You made a LOSS of Rs. {loss}")

else:
    print("No profit, no loss.")
