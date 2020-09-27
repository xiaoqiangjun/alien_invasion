import sys

import pygame
from bullet import Bullet


def check_keydown(event, ai_settings, screen, ship, bullets):
    """按键按下事件"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE:
        # 创建一颗子弹，并将其加入到编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup(event, ship):
    """按键松开事件"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = False
    elif event.key == pygame.K_LEFT:
        ship.move_left = False


def check_events(ai_settings, screen, ship, bullets):
    """监听键盘和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕图像，切换到新屏幕"""
    # 绘制
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # 显示绘制
    pygame.display.flip()