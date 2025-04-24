import pygame
from settings import WIDTH, PLAYER_WIDTH, PLAYER_HEIGHT, player_speed, WHITE, HEIGHT

class Player:
    def __init__(self):
        self.rect = pygame.Rect(
            (WIDTH - PLAYER_WIDTH) // 2,
            HEIGHT - PLAYER_HEIGHT - 10,
            PLAYER_WIDTH, PLAYER_HEIGHT
        )

    def move(self, dx):
        self.rect.x += dx * player_speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)
