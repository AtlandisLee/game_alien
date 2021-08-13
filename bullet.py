# -*- coding: utf-8 -*-
"""
作者：AtlandisLee
日期：2021年08月14日
"""
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        super.__init__()

        self.screen=ai_game.screen
        self.speed=ai_game.settings.bullet_speed
        self.width=ai_game.settings.bullet_width
        self.height=ai_game.settings.bullet_height
        self.color=ai_game.settings.bullet_color

        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.midtop=ai_game.ship.rect.midtop

        self.y=float(self.rect.y)

    def update(self):
        self.y -= self.speed
        self.rect.y=self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
