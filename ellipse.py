#Import packages
import pygame
import math

#Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 255)
COLOR_LIST = [GREEN, PURPLE, RED, BLUE]
RECT = [100, 100, 250, 200]
#pi is math.pi

#Window init
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Hello Game")

done = False
clock = pygame.time.Clock()
#Game loop
while not done:
    #Main Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #Game logic
    #Drawing
    screen.fill(WHITE) #Clear screen
    pygame.draw.rect(screen, BLACK, RECT, 2)
    angle_s = 0
    angle_e = (math.pi / 2)
    for i in range(0, 4):
        pygame.draw.arc(screen, COLOR_LIST[i], RECT, angle_s, angle_e, 2)
        angle_s += math.pi / 2
        angle_e += math.pi / 2
    pygame.display.flip() #Update screen
    clock.tick(60) #60 fps
    
pygame.quit()

print("Done")