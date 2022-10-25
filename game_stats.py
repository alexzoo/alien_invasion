from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats:
    """отслеживание статистики для игры"""

    def __init__(self, ai_game: AlienInvasion):
        """инициализируем статистику"""
        self.settings = ai_game.settings
        self.reset_stats()
        # игра запускается в активном состоянии
        self.game_active = True

    def reset_stats(self):
        """инициализирует статистику, изменяющуюся в ходе игры"""
        self.ships_left = self.settings.ship_limit


