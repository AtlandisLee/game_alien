# -*- coding: utf-8 -*-
"""
作者：AtlandisLee
日期：2021年08月17日
"""


class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False

        self.highest_score = 0

    def reset_stats(self):
        self.ships_remain = self.settings.ship_limit
        self.score = 0
