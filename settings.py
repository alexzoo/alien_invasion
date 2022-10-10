class Settings:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализируем настройки игры"""
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # скорость перемещения кораблем
        self.ship_speed = 5

        # параметры снаряда
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3


