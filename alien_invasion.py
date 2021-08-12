# -*- coding: utf-8 -*-
"""
作者：AtlandisLee
日期：2021年08月06日
"""
# 创建Pygame窗口及响应用户输入

import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()

        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,
                                             self.settings.screen_height))

        self.ship=Ship(self)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        while True:
            self._check_event()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        self.screen.blit(self.settings.bg_image,(0,0))
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

