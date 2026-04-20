import pygame
from tools import draw_rect, draw_circle

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

color = BLACK
tool = "brush"

drawing = False
start_pos = None

screen.fill(WHITE)

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

            end_pos = event.pos

            if tool == "rect":
                draw_rect(screen, color, start_pos, end_pos)

            if tool == "circle":
                draw_circle(screen, color, start_pos, end_pos)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_b:
                tool = "brush"

            if event.key == pygame.K_e:
                tool = "eraser"

            if event.key == pygame.K_r:
                tool = "rect"

            if event.key == pygame.K_c:
                tool = "circle"

            if event.key == pygame.K_1:
                color = BLACK
            if event.key == pygame.K_2:
                color = RED

    if drawing and tool == "brush":
        pygame.draw.circle(screen, color, pygame.mouse.get_pos(), 5)

    if drawing and tool == "eraser":
        pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), 10)

    pygame.display.update()

pygame.quit()