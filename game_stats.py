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

        self._local_highest_score()

    def reset_stats(self):
        self.ships_remain = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _local_highest_score(self):
        with open('history highest score.txt', 'r') as loc:
            self.highest_score = int(loc.read())
