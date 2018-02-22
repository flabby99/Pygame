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
#Game loop
while not done:
    #Main Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #Game logic
    #Drawing
    screen.fill(WHITE) #Clear screen
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)
    pygame.display.flip() #Update screen
    clock.tick(60) #60 fps
    
pygame.quit()

print("Done")