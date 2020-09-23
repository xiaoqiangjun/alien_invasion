import sys

import pygame
from settings import Settings

def run_game():
    # 初始化pygame、设置与屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("alien invasion")

    # 游戏主循环
    while True:

        # 监听键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 填充背景色
        screen.fill(ai_settings.bg_color)

        # 显示绘制
        pygame.display.flip()

run_game()