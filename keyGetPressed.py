import pygame

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

run = True
while run:
    
    key = pygame.key.get_pressed()
    if key[pygame.K_z] == True and key[pygame.K_LSHIFT] == True:
        print("Sprinting")
    elif key[pygame.K_z] == True:
        print("Running")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

pygame.quit()