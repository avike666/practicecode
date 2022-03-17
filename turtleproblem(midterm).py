import turtle

def drawStar(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    for i in range(7):
        turtle.forward(280)
        turtle.left(160)
        turtle.forward(280)

drawStar(0, 0)
