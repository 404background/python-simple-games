import pygame
from settings import BULLET_WIDTH, BULLET_HEIGHT, bullet_speed, RED

class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BULLET_WIDTH, BULLET_HEIGHT)

    def update(self):
        self.rect.y -= bullet_speed

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)
