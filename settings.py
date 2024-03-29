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

        # 飞船设置
        self.ship_speed = 1.0
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_magazine = 5

        # 外星人设置
        self.alien_y_drop = 10
        self.fleet_xdirection = 1

        self.speedup_scale = 1.2
        self.scoreup_scale = 2

    def init_level(self):
        self.ship_speed = 1.0
        self.bullet_speed = 1.5
        self.alien_speed = 0.3

        self.alien_points = 50

        self.fleet_xdirection = 1

    def level_up(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points *= self.scoreup_scale
