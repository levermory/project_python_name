import sys
import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
	for event in pygame.event.get():  # обработка ивентов, созданных пользователем 
		if event.type == pygame.QUIT:  # выход из игры
			sys.exit()

		if event.type == pygame.KEYDOWN:  # обработка нажатия кнопки и изменение флажка при нажатии
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		if event.type == pygame.KEYUP:  # обработка отпускания клавиши, в результате чего присваивается значение False флажку
			check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, aliens, bullets, background_image):
    screen.blit(background_image, [0,0])  # Перерисовка экрана
    for bullet in bullets.sprites():  # Все пули выводятся позади изображений корабля
        bullet.draw_bullet()
    ship.blitme()  # рисуем корабль
    aliens.draw(screen)  # рисуем корабль
    pygame.display.flip()  # Отображение последнего прорисованного экрана.

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    if event.key == pygame.K_SPACE:
    	fire_bullet(ai_settings, screen, ship, bullets)
    if event.key == pygame.K_ESCAPE:
    	sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False
    if event.key == pygame.K_UP:
        ship.moving_up = False

def update_bullets(bullets):  # Обновление позиции пули и их удаление
    bullets.update()
    for bullet in bullets.copy():
    	if bullet.rect.bottom <= 0:
    		bullets.remove(bullet)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width  # Кол-во прищельцев в ряду
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):  # Создание корабля пришельцев
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):  # определяем число ряядов пришельцев
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_fleet(ai_settings, screen, ship, aliens):  # создание флота пришельцев
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):  # Создание первого ряда пришельцев
        for alien_number in range(number_aliens_x):
        	create_alien(ai_settings, screen, aliens, alien_number, row_number)

def check_fleet_edges(ai_settings, aliens):  # достижение правого края экрана
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):  # Опускает флот и меняет его напрапвление 
    for alien in aliens.sprites():
    	alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def update_aliens(ai_settings, aliens):  # Обновление позиции пришельцев во флоте
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

