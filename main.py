import pygame, sys

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

GREY = (29, 29, 27)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #BASIC SCRREN CREATED
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock() #Needed for framerate

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        #Drawing a color in the screen
        screen.fill(GREY)


    pygame.display.update()
    clock.tick(60) #Clock will run 60 times each second