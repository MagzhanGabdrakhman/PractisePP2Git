import pygame
import random

class Coin:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(50, 350), -50, 20, 20)

    def update(self, speed):
        self.rect.y += speed

        if self.rect.y > 600:
            self.rect.y = -50
            self.rect.x = random.randint(50, 350)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 215, 0), self.rect.center, 10)