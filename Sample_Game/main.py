#Note as of 22-02-2018 I clearly must have been drunk when I made this
#If you click prepare to be deafened with De Niro haha

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
    pygame.mouse.set_visible(False)
    #Image loading
    background_image = pygame.image.load("background.jpg").convert()
    player_image = pygame.image.load("cat.png").convert()
    player_image.set_colorkey((78, 58, 33)) #makes that color transparent
    #Sound loading
    click_sound = pygame.mixer.Sound("come_out.wav")
    #Game loop
    while not done:
        #Main Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()
        #Game logic
        player_position = pygame.mouse.get_pos()
        x = player_position[0]
        y = player_position[1]
        #Drawing
        #screen.fill(WHITE) #Clear screen
        screen.blit(background_image, [0,0])
        screen.blit(player_image, [x,y])
        pygame.display.flip() #Update screen
        clock.tick(60) #60 fps

    pygame.quit()

if __name__ == "__main__":
    main()
