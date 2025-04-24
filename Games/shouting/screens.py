import pygame, sys
from settings import WIDTH, HEIGHT, BLACK, WHITE

def start_screen():
    # Use a Japanese font that exists on your system, e.g. "msgothic" or "meiryo"
    font_large = pygame.font.SysFont("msgothic", 48)
    font_small = pygame.font.SysFont("msgothic", 24)
    screen = pygame.display.get_surface()
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
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    # Set the difficulty speed in settings
                    import settings
                    settings.DIFFICULTY_SPEED = 0.3
                    waiting = False
                elif event.key == pygame.K_2:
                    import settings
                    settings.DIFFICULTY_SPEED = 3
                    waiting = False

def game_over_screen(score):
    font_large = pygame.font.SysFont("msgothic", 48)
    font_small = pygame.font.SysFont("msgothic", 24)
    screen = pygame.display.get_surface()
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
    return
