import sys
import pygame

def check_events(ship):
	for event in pygame.event.get():  # обработка ивентов, созданных пользователем 
		if event.type == pygame.QUIT:  # выход из игры
			sys.exit()

		if event.type == pygame.KEYDOWN:  # обработка нажатия кнопки и изменение флажка при нажатии
			check_keydown_events(event, ship)

		if event.type == pygame.KEYUP:  # обработка отпускания клавиши, в результате чего присваивается значение False флажку
			check_keyup_events(event, ship)

def update_screen(background_image, screen, ship):
    screen.blit(background_image, [0,0])  # Перерисовка экрана
    ship.blitme()  # рисуем корабль
    pygame.display.flip()  # Отображение последнего прорисованного экрана.

def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    if event.key == pygame.K_UP:
        ship.moving_up = False