import pygame, sys
from spaceship import Spacecship #Call spaceship file
#from laser import Laser

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

GREY = (29, 29, 27)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #BASIC SCRREN CREATED
pygame.display.set_caption("Python Space Invaders")

clock = pygame.time.Clock() #Needed for framerate

spaceship = Spacecship(SCREEN_WIDTH, SCREEN_HEIGHT) #Initialize spaceship in the position given width and height
spaceship_group = pygame.sprite.GroupSingle() #Start a group
spaceship_group.add(spaceship)


#Used to check the behavior of the laser movement
#laser = Laser((100,100), 6, SCREEN_HEIGHT)
#lasers_group = pygame.sprite.Group()
#lasers_group.add(laser)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    #Update
    spaceship_group.update()
    #lasers_group.update()
    
    #Draw
    screen.fill(GREY)
    spaceship_group.draw(screen)
    #lasers_group.draw(screen)
    spaceship_group.sprite.lasers_group.draw(screen)


    pygame.display.update()
    clock.tick(60) #Clock will run 60 times each second