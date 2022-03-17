bottles = int(input("How many bottles of paint do you need?"))
color = input("What color?")
packages = 0

def OliviaProject(bottles, color):
    if (color == "Red"):
        packages = bottles // 3
        if (bottles % 3 != 0):
            packages = packages + 1
    else:
        packages = bottles // 2
        if (bottles % 2 != 0):
            packages = packages + 1

    return packages


packages = OliviaProject(bottles, color)

print("You need ", packages, " packages of paint")


