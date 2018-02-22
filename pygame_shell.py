#Import packages
import pygame

#Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

def main():
    #Window init
    pygame.init()
    size = (1280, 720)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
        #Game logic
        #Drawing
        screen.fill(WHITE) #Clear screen
        pygame.display.flip() #Update screen
        clock.tick(60) #60 fps
        
    pygame.quit()

if __name__ == "__main__":
    main()