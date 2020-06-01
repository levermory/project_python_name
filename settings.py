class Settings():  # класс для хранения настроек игры
    def __init__(self):
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (65, 74, 76)
        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 2
        self.bullet_width = 7
        self.bullet_height = 17
        self.bullet_color = 255, 36, 0
        self.bullets_allowed = 5