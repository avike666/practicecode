import random

dice = int(input("How many dice would you like to roll?\n"))


def rollDice(dice):
    d = 0
    total = 0
    for i in range(dice):
        d = random.randint(1, 6)
        print(d)




(rollDice(dice))


