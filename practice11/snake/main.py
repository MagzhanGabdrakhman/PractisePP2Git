import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

snake = [(100, 100)]
direction = (20, 0)

food = (200, 200)
food_weight = random.choice([1, 2, 3])
food_timer = time.time()

score = 0

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = (0, -20)
    if keys[pygame.K_DOWN]:
        direction = (0, 20)
    if keys[pygame.K_LEFT]:
        direction = (-20, 0)
    if keys[pygame.K_RIGHT]:
        direction = (20, 0)

    # Движение змеи
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, head)

    # Проверка еды
    if head == food:
        score += food_weight
        food = (random.randrange(0, 600, 20), random.randrange(0, 600, 20))
        food_weight = random.choice([1, 2, 3])
        food_timer = time.time()
    else:
        snake.pop()

    # Таймер еды (5 секунд)
    if time.time() - food_timer > 5:
        food = (random.randrange(0, 600, 20), random.randrange(0, 600, 20))
        food_timer = time.time()

    # Отрисовка
    for segment in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*segment, 20, 20))

    pygame.draw.rect(screen, (255, 0, 0), (*food, 20, 20))

    pygame.display.update()
    clock.tick(10)