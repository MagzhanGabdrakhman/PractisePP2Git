import pygame
from snake import Snake
from food import generate_food
from settings import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = Snake()
food = generate_food(snake.body, WIDTH, HEIGHT)

score = 0
level = 1
speed = 10

font = pygame.font.SysFont(None, 30)

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake.dx, snake.dy = -20, 0
    if keys[pygame.K_RIGHT]:
        snake.dx, snake.dy = 20, 0
    if keys[pygame.K_UP]:
        snake.dx, snake.dy = 0, -20
    if keys[pygame.K_DOWN]:
        snake.dx, snake.dy = 0, 20

    snake.move()

    head = snake.body[0]

    # wall collision
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        running = False

    # eat food
    if head == food:
        snake.grow()
        food = generate_food(snake.body, WIDTH, HEIGHT)
        score += 1

        if score % 3 == 0:
            level += 1
            speed += 2

    # draw snake
    for block in snake.body:
        pygame.draw.rect(screen, (0,255,0), (*block, 20, 20))

    pygame.draw.rect(screen, (255,0,0), (*food, 20, 20))

    screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (10,10))
    screen.blit(font.render(f"Level: {level}", True, (255,255,255)), (10,40))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit(0)