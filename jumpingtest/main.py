import pygame
from pygame.locals import *
import sys

pygame.init()

CLOCK = pygame.time.Clock()           
SCREEN = pygame.display.set_mode((1500, 792))
pygame.display.set_caption("Plateformer")

X_POSITION, Y_POSITION = 50, 450

Y_GRAVITY = 1
JUMP_HEIGHT = 20
Y_VELOCITY = JUMP_HEIGHT

jumping = False

STANDING_SURFACE = pygame.image.load("link.png").convert_alpha()
JUMPING_SURFACE = pygame.image.load("linkJump.png").convert_alpha()
BACKGROUND = pygame.image.load("map.jpg").convert()

link_rect = STANDING_SURFACE.get_rect(center=(X_POSITION,Y_POSITION))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys_pressed = pygame.key.get_pressed()
    
    if keys_pressed[pygame.K_SPACE]:
        jumping = True
        

    SCREEN.blit(BACKGROUND, (0, 0))
    
    if jumping:
        Y_POSITION -= Y_VELOCITY
        Y_VELOCITY -= Y_GRAVITY
        if Y_VELOCITY < -JUMP_HEIGHT:
            jumping = False
            Y_VELOCITY = JUMP_HEIGHT
        link_rect = JUMPING_SURFACE.get_rect(center=(X_POSITION,Y_POSITION))           
        SCREEN.blit(JUMPING_SURFACE,link_rect)
    else:
        link_rect = STANDING_SURFACE.get_rect(center=(X_POSITION,Y_POSITION))           
        SCREEN.blit(STANDING_SURFACE,link_rect)
        
    pygame.display.update()
    CLOCK.tick(60)

pygame.quit()