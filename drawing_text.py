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
#True, False for bold and italics respectively
font = pygame.font.SysFont("comicsansms", 50, True, False)
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
    text = font.render("My text", True, BLACK) #True - anti-aliased
    screen.blit(text, [300, 300])
    score = 15
    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, [250, 250])
    pygame.display.flip() #Update screen
    clock.tick(60) #60 fps
    
pygame.quit()

print("Done")