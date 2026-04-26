import pygame
import random

pygame.init()

# Размер экрана
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer with Coins")

clock = pygame.time.Clock()

# Игрок
player = pygame.Rect(250, 600, 50, 80)

# Враг
enemy = pygame.Rect(random.randint(0, 550), 0, 50, 80)
enemy_speed = 5

# Монета
coin = pygame.Rect(random.randint(0, 550), -100, 30, 30)
coin_weight = random.choice([1, 2, 3])  # вес монеты

score = 0

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # Движение врага
    enemy.y += enemy_speed
    if enemy.y > HEIGHT:
        enemy.y = 0
        enemy.x = random.randint(0, 550)

    # Движение монеты
    coin.y += 5
    if coin.y > HEIGHT:
        coin.y = -100
        coin.x = random.randint(0, 550)
        coin_weight = random.choice([1, 2, 3])

    # Сбор монеты
    if player.colliderect(coin):
        score += coin_weight  # добавляем вес
        coin.y = -100

        # Увеличение скорости каждые 5 очков
        if score % 5 == 0:
            enemy_speed += 1

    # Столкновение с врагом
    if player.colliderect(enemy):
        running = False

    # Отрисовка
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)
    pygame.draw.rect(screen, (255, 215, 0), coin)

    pygame.display.update()
    clock.tick(60)