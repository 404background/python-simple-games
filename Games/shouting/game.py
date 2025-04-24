# -*- coding: utf-8 -*-
import pygame, sys
from settings import WIDTH, HEIGHT, BLACK, SCORE_MAPPING, BULLET_WIDTH, BULLET_HEIGHT
from player import Player
from bullet import Bullet
from enemy import Enemy
from screens import start_screen, game_over_screen

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")
clock = pygame.time.Clock()

def main():
    while True:  # Outer loop for returning to the title screen after game over
        start_screen()
        player = Player()
        bullets = []
        enemies = [Enemy()]
        font = pygame.font.SysFont("msgothic", 24)
        score = 0
        last_spawn_time = pygame.time.get_ticks()
        spawn_interval = 1000  # milliseconds
        running = True
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        bullet_x = player.rect.centerx - BULLET_WIDTH // 2
                        bullet_y = player.rect.top - BULLET_HEIGHT
                        bullets.append(Bullet(bullet_x, bullet_y))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move(-1)
            if keys[pygame.K_RIGHT]:
                player.move(1)
            if pygame.time.get_ticks() - last_spawn_time >= spawn_interval:
                enemies.append(Enemy())
                last_spawn_time = pygame.time.get_ticks()

            for bullet in bullets[:]:
                bullet.update()
                if bullet.rect.bottom < 0:
                    bullets.remove(bullet)
                else:
                    for enemy in enemies[:]:
                        if bullet.rect.colliderect(enemy.rect):
                            bullets.remove(bullet)
                            enemies.remove(enemy)
                            score += SCORE_MAPPING.get(enemy.color, 1)
                            enemies.append(Enemy())
                            break

            for enemy in enemies[:]:
                enemy.update()
                if enemy.rect.bottom >= HEIGHT:  # Enemy reached bottom: game over
                    game_over_screen(score)
                    running = False
                    break
                elif enemy.rect.colliderect(player.rect):
                    game_over_screen(score)
                    running = False
                    break

            screen.fill(BLACK)
            instructions = font.render("←/→キーで移動、スペースキーで発射", True, (255, 255, 255))
            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            screen.blit(instructions, (10, 10))
            screen.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))
            player.draw(screen)
            for enemy in enemies:
                enemy.draw(screen)
            for bullet in bullets:
                bullet.draw(screen)
            pygame.display.flip()
        # After game over, outer loop shows title screen again.

if __name__ == "__main__":
    main()
