import sys

import pygame
from bullet import Bullet
from alien import Alien


def check_keydown(event, ai_settings, screen, ship, bullets):
    """按键按下事件"""
    if event.key == pygame.K_RIGHT:
        ship.move_right = True
    elif event.key == pygame.K_LEFT:
        ship.move_left = True
    elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕图像，切换到新屏幕"""
    # 绘制
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    # 显示绘制
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """更新子弹删除子弹"""
    bullets.update()

    # 删除越界子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove((bullet))

    Checfk_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def Checfk_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """相应子弹击中外星人"""
    # 检测击中
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # 删除子弹，生成新外星人
        aliens.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """没有到限制，就创建一颗子弹，并将其加入到编组bullets中"""  #
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_rows(ai_settings, ship_height, alien_height):
    """计算外星人行数"""
    available_space_y = ai_settings.screen_height - (
        3 * alien_height) - ship_height
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens_x(ai_settings, alien_width):
    """计算一行可以放几个外星人"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，间距为外星人宽度
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    # 创建第一个外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """外星人到边缘"""
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """下移，反向"""
    for alien in aliens:
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, ship, aliens):
    """检查边缘，更新所有外星人位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人与飞船碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        print('666')