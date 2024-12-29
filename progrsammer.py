#This file model for different programm excersice.

array = [1,8,4,2,15,11,12,9,0]

my_min = min(array)
my_max = max(array)

print(f"min = {my_min} max = {my_max}")




array = [1,8,4,2,15,11,12,9,0]
array.sort()

my_min = array[0]
my_max = array[-1]

print(f"min = {my_min} max = {my_max}")



array = [1,8,4,2,15,11,12,9,0]
a = sorted(array)

my_min = a[0]
my_max = a[-1]

print(f"min = {my_min} max = {my_max}")



#Вводится натуральное число N. Требуется найти сумму его цифр 

n = int(input("please,enter a number "))

left_digit = n // 10
right_digit = n % 10

a = left_digit + right_digit

print(a)


#Вводится трехзначное натуральное число N. Требуется найти сумму его цифр

n = int(input("please,enter a number "))

digit1 = n // 100
digit2 = (n - digit1 * 100) // 10
digit3 = n % 10

a = digit1 + digit2 + digit3


print(digit1,digit2,digit3)








def is_lucky(number: int):
    ## number состоит из 6 цифр. Первым делом вычленим левую и правую часть.
    ## левая и правая части должны состоять из 3 цифр

    ## затем обработаем сначала левую часть и разобьем число из 3 знаков на 3 отдельных числа
    ## сложим их

    ## аналогично сделаем для правой части

    ## сравним их суммы
    left = number // 1000
    right = number % 1000

    sum_left = (left // 100) + (left % 100) // 10 + (left % 10)

    sum_right = (right // 100) + (right % 100) // 10 + (right % 10)

  
    print(f'left = {left} right = {right}')
    print(f"sum_right = {sum_right} and sum_left = {sum_left}")
    if sum_left == sum_right:
        print("You are win lucky ticket!")
    else:
        print("Sorry you aren't win lucky ticket.")


number = 556325

is_lucky(number)


def lucky_ticket():
    n = 0
    for i1 in range(0,10):
        for i2 in range(0,10):
            for i3 in range(0,10):
                for i4 in range(0,10):
                    for i5 in range(0,10):
                        for i6 in range(0,10):
                            if i1 + i2 + i3 == i4 + i5 + i6:
                                n += 1
    return n - 1
print(lucky_ticket())




number= 1234

a = str(number)

b = a[3] + a[1:3] + a[0 : 1]
print(b)









import pygame

# инициализируем библиотеку Pygame
pygame.init()

# определяем размеры окна
window_size = (300, 300)

# задаем название окна
pygame.display.set_caption("Синий фон")

# создаем окно
screen = pygame.display.set_mode(window_size)

# задаем цвет фона
background_color = (0, 0, 255)  # синий

# заполняем фон заданным цветом
screen.fill(background_color)

# обновляем экран для отображения изменений
pygame.display.flip()

# показываем окно, пока пользователь не нажмет кнопку "Закрыть"
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()





import pygame

pygame.init()
pygame.display.set_caption('Измени цвет фона')
window_surface = pygame.display.set_mode((300, 300))
background = pygame.Surface((300, 300))
background.fill(pygame.Color('#000000'))

color_list = [
    pygame.Color('#FF0000'),  # красный
    pygame.Color('#00FF00'),  # зеленый
    pygame.Color('#0000FF'),  # синий
    pygame.Color('#FFFF00'),  # желтый
    pygame.Color('#00FFFF'),  # бирюзовый
    pygame.Color('#FF00FF'),  # пурпурный
    pygame.Color('#FFFFFF')   # белый
]

current_color_index = 0

button_font = pygame.font.SysFont('Verdana', 15) # используем шрифт Verdana
button_text_color = pygame.Color("black")
button_color = pygame.Color("gray")
button_rect = pygame.Rect(100, 115, 100, 50)
button_text = button_font.render('Нажми!', True, button_text_color)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                current_color_index = (current_color_index + 1) % len(color_list)
                background.fill(color_list[current_color_index])

        window_surface.blit(background, (0, 0))
        pygame.draw.rect(window_surface, button_color, button_rect)
        button_rect_center = button_text.get_rect(center=button_rect.center)
        window_surface.blit(button_text, button_rect_center)
        pygame.display.update()




import pygame
 
pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 30
y = 30
 
while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        if is_blue: color = (0, 128, 255)
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()










import pygame
import math
import time
 
# Ignore these 3 functions. Scroll down for the relevant code. 
 
def create_background(width, height):
        colors = [(255, 255, 255), (212, 212, 212)]
        background = pygame.Surface((width, height))
        tile_width = 20
        y = 0
        while y < height:
                x = 0
                while x < width:
                        row = y // tile_width
                        col = x // tile_width
                        pygame.draw.rect(
                                background, 
                                colors[(row + col) % 2],
                                pygame.Rect(x, y, tile_width, tile_width))
                        x += tile_width
                y += tile_width
        return background
 
def is_trying_to_quit(event):
        pressed_keys = pygame.key.get_pressed()
        alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
        x_button = event.type == pygame.QUIT
        altF4 = alt_pressed and event.type == pygame.KEYDOWN and event.key == pygame.K_F4
        escape = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        return x_button or altF4 or escape
 
def run_demos(width, height, fps):
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('press space to see next demo')
        background = create_background(width, height)
        clock = pygame.time.Clock()
        demos = [
                do_rectangle_demo,
                do_circle_demo,
                do_horrible_outlines,
                do_nice_outlines,
                do_polygon_demo,
                do_line_demo
                ]
        the_world_is_a_happy_place = 0
        while True:
                the_world_is_a_happy_place += 1
                for event in pygame.event.get():
                        if is_trying_to_quit(event):
                                return
                        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                                demos = demos[1:]
                screen.blit(background, (0, 0))
                if len(demos) == 0:
                        return
                demos[0](screen, the_world_is_a_happy_place)
                pygame.display.flip()
                clock.tick(fps)
 
# Everything above this line is irrelevant to this tutorial. 
 
def do_rectangle_demo(surface, counter):
        left = (counter // 2) % surface.get_width()
        top = (counter // 3) % surface.get_height()
        width = 30
        height = 30
        color = (128, 0, 128) # purple 
        
        # Draw a rectangle 
        pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height))
 
def do_circle_demo(surface, counter):
        x = surface.get_width() // 2
        y = surface.get_height() // 2
        max_radius = min(x, y) * 4 // 5
        radius = abs(int(math.sin(counter * 3.14159 * 2 / 200) * max_radius)) + 1
        color = (0, 140, 255) # aquamarine 
        
        # Draw a circle 
        pygame.draw.circle(surface, color, (x, y), radius)
 
def do_horrible_outlines(surface, counter):
        color = (255, 0, 0) # red 
        
        # draw a rectangle 
        pygame.draw.rect(surface, color, pygame.Rect(10, 10, 100, 100), 10)
 
        # draw a circle 
        pygame.draw.circle(surface, color, (300, 60), 50, 10)
        
def do_nice_outlines(surface, counter):
        color = (0, 128, 0) # green 
        
        # draw a rectangle 
        pygame.draw.rect(surface, color, pygame.Rect(10, 10, 100, 10))
        pygame.draw.rect(surface, color, pygame.Rect(10, 10, 10, 100))
        pygame.draw.rect(surface, color, pygame.Rect(100, 10, 10, 100))
        pygame.draw.rect(surface, color, pygame.Rect(10, 100, 100, 10))
        
        # draw a circle 
        center_x = 300
        center_y = 60
        radius = 45
        iterations = 150
        for i in range(iterations):
                ang = i * 3.14159 * 2 / iterations
                dx = int(math.cos(ang) * radius)
                dy = int(math.sin(ang) * radius)
                x = center_x + dx
                y = center_y + dy
                pygame.draw.circle(surface, color, (x, y), 5)
 
 
def do_polygon_demo(surface, counter):
        color = (255, 255, 0) # yellow 
        
        num_points = 8
        point_list = []
        center_x = surface.get_width() // 2
        center_y = surface.get_height() // 2
        for i in range(num_points * 2):
                radius = 100
                if i % 2 == 0:
                        radius = radius // 2
                ang = i * 3.14159 / num_points + counter * 3.14159 / 60
                x = center_x + int(math.cos(ang) * radius)
                y = center_y + int(math.sin(ang) * radius)
                point_list.append((x, y))
        pygame.draw.polygon(surface, color, point_list)
 
def rotate_3d_points(points, angle_x, angle_y, angle_z):
        new_points = []
        for point in points:
                x = point[0]
                y = point[1]
                z = point[2]
                new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
                new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
                y = new_y
                # isn't math fun, kids? 
                z = new_z
                new_x = x * math.cos(angle_y) - z * math.sin(angle_y)
                new_z = x * math.sin(angle_y) + z * math.cos(angle_y)
                x = new_x
                z = new_z
                new_x = x * math.cos(angle_z) - y * math.sin(angle_z)
                new_y = x * math.sin(angle_z) + y * math.cos(angle_z)
                x = new_x
                y = new_y
                new_points.append([x, y, z])
        return new_points
 
def do_line_demo(surface, counter):
        color = (0, 0, 0) # black 
        cube_points = [
                [-1, -1, 1],
                [-1, 1, 1],
                [1, 1, 1],
                [1, -1, 1],
                [-1, -1, -1],
                [-1, 1, -1],
                [1, 1, -1],
                [1, -1, -1]]
                
        connections = [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 0),
                (4, 5),
                (5, 6),
                (6, 7),
                (7, 4),
                (0, 4),
                (1, 5),
                (2, 6),
                (3, 7)
                ]
                
        t = counter * 2 * 3.14159 / 60 # this angle is 1 rotation per second 
        
        # rotate about x axis every 2 seconds 
        # rotate about y axis every 4 seconds 
        # rotate about z axis every 6 seconds 
        points = rotate_3d_points(cube_points, t / 2, t / 4, t / 6)
        flattened_points = []
        for point in points:
                flattened_points.append(
                        (point[0] * (1 + 1.0 / (point[2] + 3)),
                         point[1] * (1 + 1.0 / (point[2] + 3))))
        
        for con in connections:
                p1 = flattened_points[con[0]]
                p2 = flattened_points[con[1]]
                x1 = p1[0] * 60 + 200
                y1 = p1[1] * 60 + 150
                x2 = p2[0] * 60 + 200
                y2 = p2[1] * 60 + 150
                
                # This is the only line that really matters 
                pygame.draw.line(surface, color, (x1, y1), (x2, y2), 4)
                
        
run_demos(400, 300, 60)










import pygame
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False
 
font = pygame.font.SysFont("comicsansms", 72)
 
text = font.render("Hello, World", True, (0, 128, 0))
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    
    screen.fill((255, 255, 255))
    screen.blit(text,
        (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    
    pygame.display.flip()
    clock.tick(60)




import pygame
 
def make_font(fonts, size):
    available = pygame.font.get_fonts()
    # get_fonts() returns a list of lowercase spaceless font names 
    choices = map(lambda x:x.lower().replace(' ', ''), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)
    
_cached_fonts = {}
def get_font(font_preferences, size):
    global _cached_fonts
    key = str(font_preferences) + '|' + str(size)
    font = _cached_fonts.get(key, None)
    if font == None:
        font = make_font(font_preferences, size)
        _cached_fonts[key] = font
    return font
 
_cached_text = {}
def create_text(text, fonts, size, color):
    global _cached_text
    key = '|'.join(map(str, (fonts, size, color, text)))
    image = _cached_text.get(key, None)
    if image == None:
        font = get_font(fonts, size)
        image = font.render(text, True, color)
        _cached_text[key] = image
    return image
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False
 
font_preferences = [
        "Bizarre-Ass Font Sans Serif",
        "They definitely dont have this installed Gothic",
        "Papyrus",
        "Comic Sans MS"]
 
text = create_text("Hello, World", font_preferences, 72, (0, 128, 0))
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    
    screen.fill((255, 255, 255))
    screen.blit(text,
        (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    
    pygame.display.flip()
    clock.tick(60)










import pygame
 
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    x = 0
    y = 0
    mode = 'blue'
    points = []
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed 
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius 
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list 
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        
        # draw all points 
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        
        pygame.display.flip()
        
        clock.tick(60)
 
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)
 
main()








import pygame
import math

pygame.init()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Геометрические фигуры")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
pink = (255, 192, 203)

# рисуем прямоугольник
rect_x = 50
rect_y = 50
rect_width = 100
rect_height = 50
pygame.draw.rect(screen, red, (rect_x, rect_y, rect_width, rect_height))

# рисуем круг
circle_x = 200
circle_y = 75
circle_radius = 30
pygame.draw.circle(screen, green, (circle_x, circle_y), circle_radius)

# рисуем треугольник
triangle_x = 350
triangle_y = 50
triangle_width = 100
triangle_height = 100
triangle_points = [(triangle_x, triangle_y), (triangle_x + triangle_width, triangle_y),
                   (triangle_x + triangle_width / 2, triangle_y + triangle_height)]
pygame.draw.polygon(screen, blue, triangle_points)

# рисуем пятиугольник
pent_x = 500
pent_y = 100
radius = 40
sides = 5
pent_points = []
for i in range(sides):
    angle_deg = 360 * i / sides
    angle_rad = math.radians(angle_deg)
    x = pent_x + radius * math.sin(angle_rad)
    y = pent_y - radius * math.cos(angle_rad)
    pent_points.append((x, y))
pygame.draw.polygon(screen, white, pent_points)

# рисуем эллипс
ellipse_x = 100
ellipse_y = 275
ellipse_width = 150
ellipse_height = 60
pygame.draw.ellipse(screen, red, (ellipse_x, ellipse_y, ellipse_width, ellipse_height))

# горизонтальная линия
horiz_line_y = 400
pygame.draw.line(screen, blue, (50, horiz_line_y), (590, horiz_line_y), 5)

# вертикальная линия
vert_line_x = 320
pygame.draw.line(screen, green, (vert_line_x, 50), (vert_line_x, 430), 5)

# рисуем желтую звезду
yellow_star_points = [(260 - 50, 250 - 70), (310 - 50, 250 - 70), (325 - 50, 200 - 70),
                      (340 - 50, 250 - 70), (390 - 50, 250 - 70), (350 - 50, 290 - 70),
                      (365 - 50, 340 - 70), (325 - 50, 305 - 70), (285 - 50, 340 - 70),
                      (300 - 50, 290 - 70)]
pygame.draw.polygon(screen, yellow, yellow_star_points)

# рисуем окружность с квадратом внутри
circle2_x = 490
circle2_y = 350
circle2_radius = 80
pygame.draw.circle(screen, white, (circle2_x, circle2_y), circle2_radius)
square_side = 60
square_x = circle2_x - square_side / 2
square_y = circle2_y - square_side / 2
pygame.draw.rect(screen, pink, (square_x, square_y, square_side, square_side))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()







import pygame
import random

pygame.init()

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Звезды падают вниз")

black = (0, 0, 0)
white = (255, 255, 255)
pink = (255, 192, 203)

font = pygame.font.SysFont("Verdana", 15)

star_list = []
for i in range(50):
    x = random.randrange(screen_width)
    y = random.randrange(-200, -50)
    speed = random.randrange(1, 5)
    star_list.append([x, y, speed])
score = 0

freeze = False # флаг для определения момента остановки

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN: # останавливаем падение звезд по клику
            freeze = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN: # возобновляем движение вниз, если нажат Enter
                freeze = False

    if not freeze: # если флаг не активен,
        # звезды падают вниз
        for star in star_list:
            star[1] += star[2]
            if star[1] > screen_height:
                star[0] = random.randrange(screen_width)
                star[1] = random.randrange(-200, -50)
                score += 1

    # рисуем звезды, выводим результаты подсчета
    screen.fill(black)
    for star in star_list:
        pygame.draw.circle(screen, pink, (star[0], star[1]), 3)
    score_text = font.render("Упало звезд: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    # устанавливаем частоту обновления экрана
    pygame.time.Clock().tick(60)






numbers = [1, 2, 3, 4, 5]
n = []

for i in numbers:
    n.append(i ** 2)

print(n)