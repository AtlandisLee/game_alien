# -*- coding: utf-8 -*-
"""
作者：AtlandisLee
日期：2021年08月15日
"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super(Alien, self).__init__()
        self.screen =ai_game.screen

        self.image=pygame.image.load('./images/alien.bmp')
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)