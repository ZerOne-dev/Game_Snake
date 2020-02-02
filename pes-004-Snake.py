import pygame, random
from pygame.locals import *

def on_grid_random():
    x = random.randint(0, 780)
    y = random.randint(0, 780)
    return (x // 20 * 20, y // 20 * 20)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
STOP = 4

speed = 15
score = 0

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Snake')

snake = [(200, 200)]
snake_skin = pygame.Surface((20, 20))
snake_skin.fill((255, 255, 255))

apple_pos = on_grid_random()
apple = pygame.Surface((20, 20))
apple.fill((255, 0, 0))

ant_direction = 5
my_direction = STOP


clock = pygame.time.Clock()

while True:
    clock.tick(speed)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:

            if event.key == K_SPACE:
                ant_direction = my_direction
                my_direction = STOP       
                
            if (event.key == K_UP or event.key == K_w) and my_direction != DOWN:
                if ant_direction != DOWN:
                    my_direction = UP
                    ant_direction = 5

            if (event.key == K_DOWN or event.key == K_s) and my_direction != UP:
                if ant_direction != UP:
                    my_direction = DOWN
                    ant_direction = 5
                
            if (event.key == K_RIGHT or event.key == K_d) and my_direction != LEFT:
                if ant_direction != LEFT:
                    my_direction = RIGHT
                    ant_direction = 5

            if (event.key == K_LEFT or event.key == K_a) and my_direction != RIGHT:
                if ant_direction != RIGHT:
                    my_direction = LEFT
                    ant_direction = 5         
            
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))
            
        if score < 20:
            score += 1
            if score == 2:
                speed = 16
            elif score == 5:
                speed = 17
            elif score == 10:
                speed = 18
            elif score == 15:
                speed = 20
        else:
            speed = 25
    if my_direction != STOP:    
        for i in range(len(snake) - 1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])

    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 20)
    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 20)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 20, snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 20, snake[0][1])

    
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    
    for pos in snake:
        screen.blit(snake_skin, pos)
    
    end_test = snake[0]
    end1 = end_test[0]
    end2 = end_test[1]

    if end1 >= 800:
        pygame.quit()
        # snake[0] = [0, end2]
    if end1 < 0:
        pygame.quit()
        # snake[0] = [800, end2]
    if end2 >= 800:
        pygame.quit()
        # snake[0] = [end1, 0]
    if end2 < 0:
        pygame.quit()
        # snake[0] = [end1, 800]

    for x in range(len(snake) - 1, 1, -1):
        if snake[0][0] == snake[x][0] and snake[0][1] == snake[x][1]:
            bat = snake[x]        
            if collision(snake[0],bat):
                screen.fill((250, 0, 0))
                pygame.display.update()
                pygame.quit()
            
    pygame.display.update()
    