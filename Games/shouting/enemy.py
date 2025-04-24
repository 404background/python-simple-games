import pygame, random
from settings import WIDTH, ENEMY_WIDTH, ENEMY_HEIGHT, enemy_speed, DIFFICULTY_SPEED, SCORE_MAPPING

class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(
            random.randint(0, WIDTH - ENEMY_WIDTH),
            -ENEMY_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT
        )
        self.direction = random.choice([-1, 1])
        self.color = random.choice(list(SCORE_MAPPING.keys()))
        # Faster descent for higher-scoring enemies
        self.speed_y = DIFFICULTY_SPEED * SCORE_MAPPING.get(self.color, 1)

    def update(self):
        self.rect.x += self.direction * enemy_speed
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.direction *= -1
        self.rect.y += self.speed_y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
