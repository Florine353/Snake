import random
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode([600, 600])
clock = pygame.time.Clock()
direction = [1, 0]
a = random.randint(0,30)
b = random.randint(0,30)
fruit = [a,b]

screen.fill([255,255,255])
snake = [[10,15],[11,15],[12,15]]
color_snake=[0,255,0]
for x, y in snake:
    rect = [x*20, y*20, 20, 20]
    pygame.draw.rect(screen, color_snake, rect) 

def fond(x, y):
    screen.fill([255, 255, 255])
    color_fruit = [0, 0, 0]
    rect_f = [x*20, y*20, 20, 20]
    pygame.draw.rect(screen, color_fruit, rect_f)

def move(direction, x, y):
    fond(x, y)
    for i in range (1,len(snake)):
        snake[len(snake) - i ] = snake[len(snake)-i-1]
    snake[0] = [snake[0][0] + direction[0], snake[0][1] + direction[1]]
    for x, y in snake:
        rect = [x*20, y*20, 20, 20]
        pygame.draw.rect(screen, color_snake, rect) 

while True:
    move(direction, a, b)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = [0,-1] 
            if event.key == pygame.K_DOWN:
                direction = [0,1] 
            if event.key == pygame.K_RIGHT:
                direction =  [1,0]
            if event.key == pygame.K_LEFT:
                direction = [-1,0]
    
    if snake[0] == fruit :
        a = random.randint(0,30)
        b = random.randint(0,30)
        fruit = [a, b]
        snake.append(snake[-1])
        move(direction, a, b)
    
    if snake[0] in snake[3:]:
        pygame.quit()
        sys.exit()
    
    if snake[0][0] == -1 or snake[0][0] == 30 or snake[0][1] == -1 or snake[0][1] == 30:
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(5)




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
    

