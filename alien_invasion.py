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
from bullet import Bullet


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        #窗口游戏
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        # 全屏游戏
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        pygame.display.set_caption("Alien Invasion")

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            # 这里之所以可以使用elif 代码块，是因为每个事件都只与一个键相关联。
            # 如果玩家同时按下左右箭头键，将检测到两个不同的事件。

    def _check_keydown_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        if len(self.bullets)<self.settings.bullet_magazine:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_magazine(self):
        for bullet in self.bullets.copy():
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        self.screen.blit(self.settings.bg_image, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_event()
            self.ship.update()
            self.bullets.update()
            self._check_magazine()
            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
