import pygame
from pygame.locals import *
import sys 
from game import GameObject

pygame.init()

screen = pygame.display.set_mode((1640, 1480))
clock = pygame.time.Clock()            #get a pygame clock object
player = pygame.image.load("coureur128.png").convert_alpha()
entity = pygame.image.load("alien.png").convert_alpha()
background = pygame.image.load("terrain.jpg").convert()

screen.blit(background, (0, 0))

objects = []

p = GameObject(player, 10, 3)          #create the player object

for x in range(10):                    #create 10 objects</i>

    o = GameObject(entity, x*40, x)

    objects.append(o)

while True:

    screen.blit(background, p.pos, p.pos)

    for o in objects:

        screen.blit(background, o.pos, o.pos)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] or keys[pygame.K_z]:

        p.move(up=True)

    if keys[pygame.K_DOWN] or keys[pygame.K_s]:

        p.move(down=True)

    if keys[pygame.K_LEFT] or keys[pygame.K_q]:

        p.move(left=True)

    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:

        p.move(right=True)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()

    screen.blit(p.image, p.pos)

    for o in objects:

        o.move()

        screen.blit(o.image, o.pos)

    pygame.display.update()

    clock.tick(60)

pygame.quit()