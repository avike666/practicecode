
tickets = int(input("How many tickets would you like to purchase?\n"))
friends = input("Are you friends with Julia?\n")
totalPrice = 0
discount = 0


def JuliasPlay(tickets, friends):
    if (tickets < 10 and friends == "No"):
        totalPrice = int(tickets * 10)
    elif (tickets >= 10 and friends == "No"):
        totalPrice = int(tickets * 8)
    elif (tickets < 10 and friends == "Yes"):
        totalPrice = int(tickets * (50/100))
    elif (tickets >= 10 and friends == "Yes"):
        totalPrice = int((tickets * 8) * 50/100)
    return totalPrice

totalPrice = JuliasPlay(tickets, friends)
print("Your cost is going to be ", totalPrice, " dollars")
