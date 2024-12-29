#Создание экрана.

import pygame
pygame.init()
# Установка размеров окна
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Танчики")
# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
# Обновление экрана
pygame.display.update()
pygame.quit()   