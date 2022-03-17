import random
random.seed(0)

dice = int(input("How many dice would you like to roll?\n"))


def rollDice(d):
    total = 0
    for i in range(d):
        total = total + random.randint(1, 6)
    return total

print(rollDice(dice))
