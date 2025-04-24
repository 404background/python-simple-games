# -*- coding: utf-8 -*-
import pygame, sys, random

# Initialize pygame and game window.
pygame.init()
WIDTH, HEIGHT = 640, 640  # 横幅を広げた
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooting Game")
clock = pygame.time.Clock()

# Player properties
PLAYER_WIDTH, PLAYER_HEIGHT = 50, 30
player_speed = 8  # プレイヤーの移動速度を速くした

# Bullet properties
BULLET_WIDTH, BULLET_HEIGHT = 5, 10
bullet_speed = 7

# Enemy properties
ENEMY_WIDTH, ENEMY_HEIGHT = 40, 30
enemy_speed = 2

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Global variables for difficulty and score mapping
DIFFICULTY_SPEED = 1  # Default (will be set via start screen)
SCORE_MAPPING = {
    (255, 0, 0): 1,
    (0, 255, 0): 2,
    (0, 0, 255): 3,
    (255, 255, 0): 4,
    (255, 0, 255): 5
}

# Player class
class Player:
    def __init__(self):
        self.rect = pygame.Rect((WIDTH - PLAYER_WIDTH) // 2, HEIGHT - PLAYER_HEIGHT - 10, PLAYER_WIDTH, PLAYER_HEIGHT)
    
    def move(self, dx):
        self.rect.x += dx * player_speed
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.right > WIDTH: self.rect.right = WIDTH

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BULLET_WIDTH, BULLET_HEIGHT)
    
    def update(self):
        self.rect.y -= bullet_speed

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

# Enemy class
class Enemy:
    def __init__(self):
        self.rect = pygame.Rect(random.randint(0, WIDTH - ENEMY_WIDTH), -ENEMY_HEIGHT, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.direction = random.choice([-1, 1])
        self.color = random.choice(list(SCORE_MAPPING.keys()))
        # 増えるスコアに応じて降下速度が速くなる
        self.speed_y = DIFFICULTY_SPEED * SCORE_MAPPING.get(self.color, 1)

    def update(self):
        self.rect.x += self.direction * enemy_speed
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.direction *= -1
        self.rect.y += self.speed_y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

def start_screen():
    global DIFFICULTY_SPEED
    # 日本語フォント "meiryo" や "msgothic" を使用（環境に応じて調整してください）
    font_large = pygame.font.SysFont("msgothic", 48)
    font_small = pygame.font.SysFont("msgothic", 24)
    screen.fill(BLACK)
    title = font_large.render("シューティングゲーム", True, WHITE)
    instr = font_small.render("開始するにはキーを押してください", True, WHITE)
    diff_instr = font_small.render("難易度を選択: 1: やさしい   2: むずかしい", True, WHITE)
    screen.blit(title, ((WIDTH - title.get_width()) // 2, HEIGHT // 4))
    screen.blit(diff_instr, ((WIDTH - diff_instr.get_width()) // 2, HEIGHT // 2 - 20))
    screen.blit(instr, ((WIDTH - instr.get_width()) // 2, HEIGHT // 2 + 20))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    DIFFICULTY_SPEED = 0.3  # やさしいの場合、落下速度をよりゆっくりに設定
                    waiting = False
                elif event.key == pygame.K_2:
                    DIFFICULTY_SPEED = 3
                    waiting = False

def game_over_screen(score):
    font_large = pygame.font.SysFont("msgothic", 48)
    font_small = pygame.font.SysFont("msgothic", 24)
    screen.fill(BLACK)
    game_over_text = font_large.render("ゲームオーバー", True, WHITE)
    score_text = font_small.render(f"スコア: {score}", True, WHITE)
    instr = font_small.render("任意のキーを押してタイトルに戻る", True, WHITE)
    screen.blit(game_over_text, ((WIDTH - game_over_text.get_width()) // 2, HEIGHT // 3))
    screen.blit(score_text, ((WIDTH - score_text.get_width()) // 2, HEIGHT // 2))
    screen.blit(instr, ((WIDTH - instr.get_width()) // 2, HEIGHT // 2 + 30))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
    # ここで終了せずに戻る
    return

def main():
    while True:  # 外側のループでタイトル画面に戻るようにする
        start_screen()
        player = Player()
        bullets = []
        enemies = [Enemy()]  # enemy list
        font = pygame.font.SysFont("msgothic", 24)
        score = 0
        last_spawn_time = pygame.time.get_ticks()
        spawn_interval = 1000  # ミリ秒単位の新規敵生成間隔
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
                if enemy.rect.bottom >= HEIGHT:  # 敵が画面下端に到達した場合
                    game_over_screen(score)
                    running = False
                    break
                elif enemy.rect.colliderect(player.rect):
                    game_over_screen(score)
                    running = False
                    break
            screen.fill(BLACK)
            instructions = font.render("←/→キーで移動、スペースキーで発射", True, WHITE)
            screen.blit(instructions, (10, 10))
            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))
            player.draw(screen)
            for enemy in enemies:
                enemy.draw(screen)
            for bullet in bullets:
                bullet.draw(screen)
            pygame.display.flip()
        # 外側ループに戻り、タイトル画面を再表示

if __name__ == "__main__":
    main()
