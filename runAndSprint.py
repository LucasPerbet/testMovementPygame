import pygame
from pygame import locals as const

pygame.init()

pygame.display.set_caption("Jeu sympa")

screen = pygame.display.set_mode((800,800))

running = False
sprinting = False

run = True

while run:
    
    for event in pygame.event.get():
        if event.type == const.QUIT or (event.type == const.KEYDOWN and event.key == const.K_ESCAPE):
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                running = True
            if event.key == pygame.K_LSHIFT:
                sprinting = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_z:
                running = False
            if event.key == pygame.K_LSHIFT:
                sprinting = False
                
    if sprinting == True and running == True:
        print("Sprinting")
    elif running == True:
        print("Running")

             
pygame.quit()
        