# -*- coding: utf-8 -*-
"""
作者：AtlandisLee
日期：2021年08月06日
"""
# 创建Pygame窗口及响应用户输入

import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # 窗口游戏
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        # 全屏游戏
        # self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)

        self.stats = GameStats(self)
        self.scoreboard = Scoreboard(self)

        self.play_button = Button(self, 'PLAY')

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        pygame.display.set_caption("Alien Invasion")

    def _create_fleet(self):
        alien_sup = Alien(self)
        alien_width, alien_height = alien_sup.rect.size
        # screen_margin = alien_width
        num_alien_x = (self.settings.screen_width - 2 * alien_width) \
                      // (2 * alien_width)
        num_rows = (self.settings.screen_height - 3 * alien_height -
                    self.ship.rect.height) // (2 * alien_height)

        for row in range(num_rows):
            for num in range(num_alien_x):
                self._add_alien(num, row)

    def _add_alien(self, num, row):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + num * 2 * alien_width
        alien.y = alien_height * (row * 2 + 1)
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def run_game(self):
        while True:
            self._check_event()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._target_hitted()
                self._check_ship_reduce()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._load_highest_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            # 这里之所以可以使用elif 代码块，是因为每个事件都只与一个键相关联。
            # 如果玩家同时按下左右箭头键，将检测到两个不同的事件。
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_posi = pygame.mouse.get_pos()
                self._check_play_button(mouse_posi)

    def _check_keydown_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            self._restart_game()

    def _restart_game(self):
        self.stats.reset_stats()
        self.scoreboard.prep_level()
        self.scoreboard.prep_score()
        self.scoreboard.prep_ships()
        self.stats.game_active = True

        self.bullets.empty()
        self.aliens.empty()

        self.settings.init_level()
        self._create_fleet()
        self.ship.recenter()

        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_magazine:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            self._load_highest_score()
            sys.exit()

    def _check_play_button(self, mouse_posi):
        if self.play_button.rect.collidepoint(mouse_posi) \
                and not self.stats.game_active:
            self._restart_game()

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)

    def _update_aliens(self):
        if self._check_fleet_edge():
            self.settings.fleet_xdirection *= -1
            for alien in self.aliens:
                alien.rect.y += self.settings.alien_y_drop
        self.aliens.update()

    def _check_fleet_edge(self):
        for alien in self.aliens:
            if alien.rect.right >= self.settings.screen_width \
                    or alien.rect.left <= 0:
                return True

    def _target_hitted(self):
        hitting = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if hitting:
            for aliens in hitting.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.prep_score()
            self.scoreboard.check_highest_score()
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.level_up()
            self.stats.level += 1
            self.scoreboard.prep_level()

    def _check_ship_reduce(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._lost_one_ship()
        for alien in self.aliens:
            if alien.rect.bottom >= self.screen.get_rect().bottom:
                self._lost_one_ship()
                break

    def _lost_one_ship(self):
        if self.stats.ships_remain > 1:
            self.stats.ships_remain -= 1
            self.scoreboard.prep_ships()

            self.bullets.empty()
            self.aliens.empty()
            sleep(0.5)

            self._create_fleet()
            self.ship.recenter()
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        # self.screen.blit(self.settings.bg_image, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        if not self.stats.game_active:
            self.play_button.draw()

        self.scoreboard.show_score()
        pygame.display.flip()

    def _load_highest_score(self):
        with open('history highest score.txt', 'w') as loc:
            loc.write(str(self.stats.highest_score))

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
