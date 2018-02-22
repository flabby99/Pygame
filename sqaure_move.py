#Import packages
import pygame
import math

#Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
#pi is math.pi

#Window init
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hello Game")

done = False
clock = pygame.time.Clock()
rect_x = rect_y = 50
rect_change_x = rect_change_y = 5
#Game loop
while not done:
    #Main Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #Game logic
    #Drawing
    screen.fill(BLACK) #Clear screen
    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, RED, [rect_x + 15, rect_y + 15, 20, 20])
    rect_x += rect_change_x
    rect_y += rect_change_y
    if rect_y > 450 or rect_y < 0:
        rect_change_y *= -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x *= -1
    pygame.display.flip() #Update screen
    clock.tick(60) #60 fps

pygame.quit()

print("Done")
