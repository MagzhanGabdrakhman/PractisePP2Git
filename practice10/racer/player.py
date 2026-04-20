import pygame

class Player:
    def __init__(self):
        self.rect = pygame.Rect(180, 500, 40, 60)

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)