import turtle

def drawSnowman(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    for i in range(1):
        turtle.circle(90)
        turtle.circle(-170)

drawSnowman(0, 0)
