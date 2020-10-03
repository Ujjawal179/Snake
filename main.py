import pygame
import random

width = 600
height = 500

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# характеристики змейки
snake_block = 10
snake_speed = 20
x1 = width / 2
y1 = height / 2
x1_change = 0
y1_change = 0
snake_List = []
lenght = 1

# координаты яблока
apple_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
apple_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

# игровое поле
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake game')
clock = pygame.time.Clock()


font_style = pygame.font.SysFont("arial", 15)
score_font = pygame.font.SysFont('arial', 25)


# вывод очков
def score(score):
    value = score_font.render('Score: ' + str(score), True, green)
    screen.blit(value, [0, 0])


# рисование змейки
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])


running = True
while running:  # цикл игры

    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False
        # движение при нажатии
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    # конец игры если выйдешь за края
    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        running = False

    x1 += x1_change
    y1 += y1_change

    screen.fill(black)  # рисует задний фон
    pygame.draw.rect(screen, red, [apple_x, apple_y, snake_block, snake_block])  # рисует яблоко

    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)

    if len(snake_List) > lenght:
        del snake_List[0]

    for x in snake_List[:-1]:
        if x == snake_Head:
            running = False

    snake(snake_block, snake_List)
    score(lenght - 1)

    pygame.display.update()

    if x1 == apple_x and y1 == apple_y:  # растет если съест яблоко
        apple_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        apple_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        lenght += 1

    clock.tick(snake_speed)  # для движения змейки

pygame.quit()
