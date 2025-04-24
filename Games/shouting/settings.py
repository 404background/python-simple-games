# -*- coding: utf-8 -*-
# Global settings and constants

WIDTH = 640
HEIGHT = 640

# Player properties
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 30
player_speed = 8

# Bullet properties
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
bullet_speed = 7

# Enemy properties
ENEMY_WIDTH = 40
ENEMY_HEIGHT = 30
enemy_speed = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Difficulty & Score mapping
DIFFICULTY_SPEED = 1  # Default (will be set via start screen)
SCORE_MAPPING = {
    (255, 0, 0): 1,
    (0, 255, 0): 2,
    (0, 0, 255): 3,
    (255, 255, 0): 4,
    (255, 0, 255): 5
}
