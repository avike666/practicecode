
tickets = int(input("How "))
friends = 0
totalPrice = 0
discount = 0


def JuliasPlay(tickets, friends):
    if (tickets < 10 and friends == "No"):
        totalPrice = tickets * 10
    elif (tickets >= 10 and friends == "No"):
        totalPrice = tickets * 8
    elif (tickets < 10 and friends == "Yes"):
        totalPrice = tickets * (50/100)
    elif (tickets >= 10 and friends == "Yes"):
        totalPrice = (tickets * 8) * 50/100
    return totalPrice

totalPrice = JuliasPlay(tickets, friends)
print(totalPrice)
