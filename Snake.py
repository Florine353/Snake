import random
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()
direction = [1, 0]

screen.fill([255,255,255])
snake = [[10,15],[11,15],[12,15]]
color_snake=[0,255,0]
for x, y in snake:
    rect = [x*20, y*20, 20, 20]
    pygame.draw.rect(screen, color_snake, rect) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print('up')
            if event.key == pygame.K_DOWN:
                print('down')  
            if event.key == pygame.K_RIGHT:
                screen.fill([255,255,255])
                snake[0][0]+=1
                snake[1][0]+=1
                snake[2][0]+=1
                for x, y in snake:
                    rect = [x*20, y*20, 20, 20]
                    pygame.draw.rect(screen, color_snake, rect) 
            if event.key == pygame.K_LEFT:
                screen.fill([255,255,255])
                snake[0][0]-=1
                snake[1][0]-=1
                snake[2][0]-=1
                for x, y in snake:
                    rect = [x*20, y*20, 20, 20]
                    pygame.draw.rect(screen, color_snake, rect)
    pygame.display.update()
    clock.tick(10)




    #red = random.randint(0, 255)
    #green = random.randint(0, 255)
    #blue = random.randint(0, 255)
    #color = [red, green, blue]
    #screen.fill(color)
    #pygame.display.update()
    #clock.tick(1)
    """x=0
    y=0
    for i in range (30):
        for j in range(30):
            x = 20*i
            y = 20*(2*j)+(i%2)*20
            width = 20
            height = 20
            rect = [x, y, width, height]
            red = 255
            green = 255
            blue = 255
            color = [red, green, blue]
            pygame.draw.rect(screen, color, rect)"""
    

