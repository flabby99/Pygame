#Import packages
import pygame

#Define constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Ball():
    """This is a class that represents a 2D ball"""
    #Can pass extra parameters into __init__
    def __init__(self):
        """This is a constructor"""
        #Attributes:
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.size = 10
        self.color = BLACK
    #Methods
    def move(self):
        """This moves the ball"""
        self.x += self.change_x
        self.y += self.change_y
    def draw(self, screen):
        """This draws the ball on to screen"""
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)
        
class Disappearing_ball(Ball):
    def __init__(self):
        super().__init__()
        self.bye = False
    def draw(self, screen):
        if(not(self.bye)):
            super().draw(screen)

def main():
    #Window init
    pygame.init()
    size = (1280, 720)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Hello Game")
    
    done = False
    clock = pygame.time.Clock()
    ball = Ball()
    ball.x = 100
    ball.y = 100
    ball.change_x = 2
    ball.change_y = 1
    ball.color = BLUE
    
    flashing_ball = Disappearing_ball()
    flashing_ball.x = flashing_ball.y = 100
    
    #Game loop
    while not done:
        #Main Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                if event.key == pygame.K_w:
                    flashing_ball.bye = not(flashing_ball.bye)
        #Game logic
        ball.move()
        #Drawing
        screen.fill(WHITE) #Clear screen
        ball.draw(screen)
        flashing_ball.draw(screen)
        pygame.display.flip() #Update screen
        clock.tick(60) #60 fps
        
    pygame.quit()

if __name__ == "__main__":
    main()