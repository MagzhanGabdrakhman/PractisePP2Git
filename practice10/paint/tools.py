import pygame

def draw_rect(screen, color, start, end):
    width = end[0] - start[0]
    height = end[1] - start[1]

    rect = pygame.Rect(start[0], start[1], width, height)
    pygame.draw.rect(screen, color, rect)


def draw_circle(screen, color, start, end):
    radius = int(((end[0] - start[0])**2 + (end[1] - start[1])**2) ** 0.5)
    pygame.draw.circle(screen, color, start, radius)