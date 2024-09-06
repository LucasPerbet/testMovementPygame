import pygame
from pygame.locals import *
import sys
from game import GameObject

pygame.init()



screen = pygame.display.set_mode((1500, 792))
clock = pygame.time.Clock()            #get a pygame clock object
player = pygame.image.load("link.png").convert_alpha()
background = pygame.image.load("map.jpg").convert()

screen.blit(background, (0, 0))

objects = []
#create the player object
p = GameObject(player, 10, 10) 
p.pos[0] = 0
p.pos[1] = 380
while True:

    screen.blit(background, p.pos, p.pos)
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] or keys[pygame.K_q]:

        p.move(left=True)

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:

        p.move(right=True)
    
    
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()

    screen.blit(p.image, p.pos)
                
    pygame.display.update()
    clock.tick(60)

pygame.quit()