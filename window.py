import pygame
import sys  # нужно для завершения игры по команде игрока
from settings import Settings  # используем наш модуль с настройками
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()  # инициализирует настройки, необходимые Pygame для нормальной работы.
    background_image = pygame.image.load('C:/Users/Edgar/Desktop/alien_invasion_game/images/background.bmp')
    ai_settings = Settings()  # создаем экземпляр класса
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), pygame.FULLSCREEN)  # задаем разрешение экрана
    pygame.display.set_caption("Alien Invasion")
    pygame.display.set_icon(pygame.image.load('C:/Users/Edgar/Desktop/alien_invasion_game/images/Jedi_Order.bmp'))
    ship = Ship(ai_settings, screen)  # Cоздание корабля
    alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)  # Отслеживание событий клавиатуры и мыши.
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets, background_image)  # обновление экрана


run_game()
