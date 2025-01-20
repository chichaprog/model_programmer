from asyncio import wait_for

import pygame
import random

# Инициализация Pygame
pygame.init()

# Константы
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 128, 255)
OBSTACLE_COLOR = (255, 0, 0)
PLAYER_RADIUS = 25
OBSTACLE_RADIUS = 25
SPEED = 5
SPEED_INCREMENT = 0.1

# Загрузка звуковых эффектов и музыки
pygame.mixer.music.load('background_music.mp3')  # Замените на путь к вашей музыке
pygame.mixer.music.play(-1)  # Зацикливаем музыку
collision_sound = pygame.mixer.Sound('collision.wav')  # Замените на путь к вашему звуковому эффекту

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Избегай шариков!")

# Игрок
player_pos = [WIDTH // 2, HEIGHT - PLAYER_RADIUS]

# Препятствия (шарики)
obstacles = []
for i in range(5):
    x_pos = random.randint(OBSTACLE_RADIUS, WIDTH - OBSTACLE_RADIUS)
    obstacles.append([x_pos, random.randint(-100, -40)])

# Счетчик очков
score = 0
font = pygame.font.Font(None, 36)

# Основной игровой цикл
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > PLAYER_RADIUS:
        player_pos[0] -= SPEED
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - PLAYER_RADIUS:
        player_pos[0] += SPEED

    # Обновление положения препятствий
    for obstacle in obstacles:
        obstacle[1] += SPEED
        if obstacle[1] > HEIGHT:
            obstacle[1] = random.randint(-100, -40)
            obstacle[0] = random.randint(OBSTACLE_RADIUS, WIDTH - OBSTACLE_RADIUS)
            score += 1  # Увеличиваем счет при успешном уклонении

    # Проверка на столкновение
    for obstacle in obstacles:
        distance = ((player_pos[0] - obstacle[0]) ** 2 + (player_pos[1] - obstacle[1]) ** 2) ** 0.5
        if distance < PLAYER_RADIUS + OBSTACLE_RADIUS:
            collision_sound.play()  # Воспроизводим звук столкновения
            score -=1
            if score <=0:
                game_over = True

    # Увеличение скорости падающих шариков по мере набора очков
    SPEED = 5 + (score * SPEED_INCREMENT)

    # Отрисовка объектов
    screen.fill(WHITE)
    pygame.draw.circle(screen, PLAYER_COLOR, (player_pos[0], player_pos[1]), PLAYER_RADIUS)
    for obstacle in obstacles:
        pygame.draw.circle(screen, OBSTACLE_COLOR, (obstacle[0], obstacle[1]), OBSTACLE_RADIUS)

    # Отображение счета на экране
    score_text = font.render(f'Счет: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()