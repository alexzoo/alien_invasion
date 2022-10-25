class Settings:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Инициализируем настройки игры"""
        # параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # настройки корабля
        self.ship_speed = 5
        self.ship_limit = 3

        # параметры снаряда
        self.bullet_speed = 15
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3

        # настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # 1 - движение вправо, -1 - влево
        self.fleet_direction = 1




