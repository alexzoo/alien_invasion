from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """класс представляющий одного пришельца"""

    def __init__(self, ai_game: AlienInvasion):
        """инициализирует пришельца и задает его начальную позицию"""
        super().__init__()
        self.screen = ai_game.screen

        # загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # сохранение точной горизонтальной позиции пришельца
        self.x = float(self.rect.x)
