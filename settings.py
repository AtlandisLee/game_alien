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
        self.bg_color = (230,230,230)
        self.bg_image = pygame.image.load('./images/Gargantua.bmp')
