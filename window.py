import pygame
import sys  # нужно для завершения игры по команде игрока
from settings import Settings  # используем наш модуль с настройками
from ship import Ship
import game_functions as gf

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()  # инициализирует настройки, необходимые Pygame для нормальной работы.
    background_image = pygame.image.load('C:/Users/Edgar/Desktop/alien_invasion_game/images/background.bmp')
    ai_settings = Settings()  # создаем экземпляр класса
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # задаем разрешение экрана
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings, screen)  # Cоздание корабля
    # Запуск основного цикла игры.
    while True:
        gf.check_events(ship)  # Отслеживание событий клавиатуры и мыши.
        ship.update()
        gf.update_screen(background_image, screen, ship)  # обновление экрана


run_game()
