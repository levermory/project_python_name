import pygame
import sys  # нужно для завершения игры по команде игрока


def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()  # инициализирует настройки, необходимые Pygame для нормальной работы.
    screen = pygame.display.set_mode((1920, 1080))  # задаем разрешение экрана
    pygame.display.set_caption("Alien Invasion")

    # Запуск основного цикла игры.
    while True:
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():  # постоянная обработка ивентов, вызываемых пользователем
            if event.type == pygame.QUIT:  # обработка случая закрытия программы
                sys.exit()

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()
        

run_game()