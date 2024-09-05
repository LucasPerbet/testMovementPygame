import pygame
from pygame.locals import *

pygame.init()

# Define the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# creating game window
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# add a title to the window
pygame.display.set_caption("Snake")

# define game variable
cell_size = 20
direction = 1 # 1 is up, 2 is right, 3 is down and 4 is left
update_snake =0 #timer


#create snake
snake_pos = [[int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT)/2]]
snake_pos.append([int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT)/2 + cell_size])
snake_pos.append([int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT)/2 + cell_size *2])
snake_pos.append([int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT)/2 + cell_size *3])

# define colours
backgroundColour = (255,200, 150)
body_inner = (50, 175, 25)
body_outer = (100,100,200)
red = (255,0,0)


# a function that define a draw screen
def draw_screen():
    screen.fill(backgroundColour)
    
# set up a loop with exit event handler
run = True
while run:
    
    # launching draw_screen function
    draw_screen()

    # iterate through events
    for event in pygame.event.get():
        
        # exit condition
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == K_ESCAPE):
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 3:
                direction = 1
            if event.key == pygame.K_RIGHT and direction != 4:
                direction = 2
            if event.key == pygame.K_DOWN and direction != 1:
                direction = 3
            if event.key == pygame.K_LEFT and direction != 2:
                direction = 4            
                
        
        if update_snake > 99:
            update_snake = 0
            snake_pos = snake_pos[-1:] + snake_pos[:-1]
        
        # heading up
            if direction == 1:
                snake_pos[0][0] = snake_pos[1][0]
                snake_pos[0][1] = snake_pos[1][1] - cell_size
            if direction == 2:
                snake_pos[0][1] = snake_pos[1][1]
                snake_pos[0][0] = snake_pos[1][0] + cell_size            
            if direction == 3:
                snake_pos[0][0] = snake_pos[1][0]
                snake_pos[0][1] = snake_pos[1][1] + cell_size        
            if direction == 4:
                snake_pos[0][1] = snake_pos[1][1]
                snake_pos[0][0] = snake_pos[1][0] - cell_size        
        
        # draw snake
        head = 1
        for x in snake_pos:
            if head == 0:
                pygame.draw.rect(screen,body_outer,(x[0],x[1],cell_size, cell_size))
                pygame.draw.rect(screen,body_inner,(x[0] + 1 ,x[1] +1,cell_size - 2, cell_size - 2))
            if head == 1:       
                pygame.draw.rect(screen,body_outer,(x[0],x[1],cell_size, cell_size))
                pygame.draw.rect(screen,red,(x[0] + 1 ,x[1] +1,cell_size - 2, cell_size - 2))
                head = 0
        
        
        
        
        # display update
        pygame.display.update()
        
        # incrementing timer
        update_snake += 1
            
# end pygame
pygame.quit() 