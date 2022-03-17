import random


charges = int(input("How many times does Olivia charge her hoverboard?\n"))
totalMiles = 0

def numberOfCharges(charges):
    if (charges == 1):
        totalMiles = random.randint(3, 5)
    elif (charges >= 1):
        totalMiles = random.randint(3, 5) * charges
    else:
        print("You need to charge your hoverboard")
    return totalMiles

totalMiles = numberOfCharges(charges)
print("The Hoverboard will cover approximately", totalMiles, " miles")
    
