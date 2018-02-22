#Import packages
import pygame
import math
import random

#Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
#pi is math.pi

#Window init
pygame.init()
size = (400, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow Falling")

done = False
clock = pygame.time.Clock()
snow_list = []
for i in range(50):
    x = random.randrange(2, 398)
    y = random.randrange(2, 398)
    snow_list.append([x,y])
#Game loop
while not done:
    #Main Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #Game logic
    #Drawing
    screen.fill(BLACK) #Clear screen
    for i in range(len(snow_list)):
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        snow_list[i][1] += 1
        if snow_list[i][1] > 400:
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            x = random.randrange(0, 400)
            snow_list[i][0] = x
    pygame.display.flip() #Update screen
    clock.tick(60) #60 fps

pygame.quit()

print("Done")
