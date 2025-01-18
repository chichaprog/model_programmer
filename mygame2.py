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
PLAYER_SIZE = 50
OBSTACLE_WIDTH = 50
OBSTACLE_HEIGHT = 50
SPEED = 5

# Создание окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Избегай препятствий!")

# Игрок
player_pos = [WIDTH // 2, HEIGHT - PLAYER_SIZE]

# Препятствия
obstacles = []
for i in range(5):
    x_pos = random.randint(0, WIDTH - OBSTACLE_WIDTH)
    obstacles.append([x_pos, random.randint(-100, -40)])

# Основной игровой цикл
clock = pygame.time.Clock()
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= SPEED
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - PLAYER_SIZE:
        player_pos[0] += SPEED

    # Обновление положения препятствий
    for obstacle in obstacles:
        obstacle[1] += SPEED
        if obstacle[1] > HEIGHT:
            obstacle[1] = random.randint(-100, -40)
            obstacle[0] = random.randint(0, WIDTH - OBSTACLE_WIDTH)

    # Проверка на столкновение
    for obstacle in obstacles:
        if (player_pos[0] < obstacle[0] + OBSTACLE_WIDTH and 
            player_pos[0] + PLAYER_SIZE > obstacle[0] and 
            player_pos[1] < obstacle[1] + OBSTACLE_HEIGHT and 
            player_pos[1] + PLAYER_SIZE > obstacle[1]):
            game_over = True

    # Отрисовка объектов
    screen.fill(WHITE)
    pygame.draw.rect(screen, PLAYER_COLOR, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))
    for obstacle in obstacles:
        pygame.draw.rect(screen, OBSTACLE_COLOR, (obstacle[0], obstacle[1], OBSTACLE_WIDTH, OBSTACLE_HEIGHT))

    pygame.display.flip()
    clock.tick(30)

