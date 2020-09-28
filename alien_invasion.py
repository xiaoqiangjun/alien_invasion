import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygame、设置与屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("alien invasion")

    # 创建一艘飞船、创建外星人编组、创建子弹编组
    ship = Ship(ai_settings, screen)
    aliens = Group()
    bullets = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 游戏主循环
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, ship, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

if __name__ == "__main__":
    run_game()