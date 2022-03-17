#6.5% tax added to all items

price = int(input("Enter the price of the item:\n"))
print("Cost of item: ", price)

price_w_tax = price * (6.5 / 100)
print("after tax: ", round(price + price_w_tax))

#money = int(input("Enter the amount in cents."))
#money = money * 1.065
#print(round(money))
