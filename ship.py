# -*- coding: utf-8 -*-
"""
作者：AtlandisLee
日期：2021年08月06日
"""
import pygame


class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # get_rect()获得元素(surface)的边框

        self.image = pygame.image.load('./images/ship.bmp')
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        # 两个rect的底部中心重合
        self.x = self.rect.x

        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # 把image画到rect里

    def update(self, ai_game):
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.x += ai_game.settings.ship_speed
        if self.moving_left and self.rect.left>0:
            self.x -= ai_game.settings.ship_speed

        self.rect.x =self.x
