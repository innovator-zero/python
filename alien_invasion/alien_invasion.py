# coding=gbk
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stas import GameStats
from button import Button


def run_game():
    # ��ʼ����pygame�����ú���Ļ����
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button = Button(ai_settings, screen, "Play")
    stats = GameStats(ai_settings)

    # ���ñ���ɫ
    bg_color = (230, 230, 230)

    # ����һ�ҷɴ�
    ship = Ship(ai_settings, screen)

    # ����һ�����ڴ洢�ӵ��ı���
    bullets = Group()

    # ����һ��������
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # ��ʼ��Ϸ����ѭ��
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


run_game()
