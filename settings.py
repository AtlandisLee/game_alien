# -*- coding: utf-8 -*-
"""
作者：AtlandisLee
日期：2021年08月06日
"""
import pygame


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.bg_image = pygame.image.load('./images/Gargantua.bmp')
        self.ship_speed = 1.0

        # 子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_magazine = 5

        # 外星人设置
        self.alien_speed = 0.3
        self.alien_y_drop = 5
        self.fleet_xdirection = 1
