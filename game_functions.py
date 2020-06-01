import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
	for event in pygame.event.get():  # обработка ивентов, созданных пользователем 
		if event.type == pygame.QUIT:  # выход из игры
			sys.exit()

		if event.type == pygame.KEYDOWN:  # обработка нажатия кнопки и изменение флажка при нажатии
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		if event.type == pygame.KEYUP:  # обработка отпускания клавиши, в результате чего присваивается значение False флажку
			check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets, background_image):
    screen.blit(background_image, [0,0])  # Перерисовка экрана
    for bullet in bullets.sprites():  # Все пули выводятся позади изображений корабля
        bullet.draw_bullet()
    ship.blitme()  # рисуем корабль
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
