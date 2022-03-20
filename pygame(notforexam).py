import pygame
import random

pygame.init()

screen = pygame.display.set_mode( [ 500, 500 ] )

running = True
x = 250
y = 0

speed = 2
vX = speed
vY = speed

while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running == False

    y += vY
    x += vX
    if (y > 490):
        vY = -speed
    if (y < 0):
        vY = speed
    if (x > 490):
        vX = -speed
    if (x < 10):
        vX = speed
    
    screen.fill( (255, 255, 255) )

    pygame.draw.circle( screen, (255, 0, 0), (x, y), 10)
    pygame.display.flip()

pygame.quit()
