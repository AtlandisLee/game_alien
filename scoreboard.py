# -*- coding: utf-8 -*-
"""
作者：AtlandisLee
日期：2021年08月17日
"""
import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard:
    def __init__(self, ai_game):
        self.ai = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.score_color = (30, 30, 30)
        self.highest_score_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_level()
        self.prep_score()
        self.prep_highest_score()
        self.prep_ships()


    def prep_score(self):
        self.score_str = "{:,}".format(self.stats.score)
        self.score_image = self.font.render(
            self.score_str, True, self.score_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = self.level_rect.bottom + 10

    def prep_highest_score(self):
        self.highest_score_str = "{:,}".format(self.stats.highest_score)
        self.highest_score_image = self.font.render(
            self.highest_score_str, True, self.highest_score_color,
            self.settings.bg_color)
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.centerx = self.screen_rect.centerx
        self.highest_score_rect.top = 20

    def check_highest_score(self):
        if self.stats.highest_score < self.stats.score:
            self.stats.highest_score = self.stats.score
        self.prep_highest_score()

    def prep_level(self):
        self.level_str = f"LEVEL:{self.stats.level}"
        self.level_image = self.font.render(
            self.level_str, True, self.score_color, self.settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 20

    def prep_ships(self):
        self.ships = Group()
        for i in range(self.stats.ships_remain):
            ship = Ship(self.ai)
            ship.rect.left = i * ship.rect.width + 10
            ship.rect.top = 20
            self.ships.add(ship)

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
