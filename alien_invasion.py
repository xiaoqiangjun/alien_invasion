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

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建子弹编组
    bullets = Group()

    # 游戏主循环
    while True:

        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()

        # 绘制与显示绘制
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()