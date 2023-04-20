import random
import pygame

pygame.init()


W, H = 500, 400


color = {'white': (255, 255, 255),
         'red': (255, 0, 0),
         'orange': (255, 128, 0),
         'yellow': (255, 255, 0),
         'green': (0, 255, 0),
         'blue': (0, 0, 255),
         'purple': (178, 102, 255),
         'pink': (255, 102, 155),
         }

base_surface = pygame.display.set_mode((W, H))
pygame.display.set_caption('Snake')
pygame.display.set_icon(pygame.image.load('image/image_snake.bmp'))

background_image = pygame.image.load('image/fon.jpg')
base_surface.blit(background_image, (0, 0))

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 12

font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):
    value = score_font.render("Your points: " + str(score), True, color['yellow'])
    base_surface.blit(value, [0, 0])

def message(msg, color):
    text = font_style.render(msg, True, color)
    base_surface.blit(text, (H/10, W/3))


def our_snake(snake_block, snake_list):
    for elem in snake_list:
        pygame.draw.rect(base_surface, color['purple'], (elem[0], elem[1], snake_block, snake_block))


def game_loop():
    game_over = False
    game_close = False

    x: float = W / 2
    y = H / 2

    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, W - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, H - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            base_surface.blit(background_image, (0, 0))
            message('You loseee!!! Enter Q to exit or C to continue', color['red'])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0
                elif event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0

        if x >= W or x < 0 or y >= H or y < 0:
            game_close = True

        x += x_change
        y += y_change

        base_surface.blit(background_image, (0, 0))
        pygame.draw.rect(base_surface, color['blue'], (food_x, food_y, snake_block, snake_block))

        snake_head = list()
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        our_snake(snake_block, snake_list)
        Your_score(length_of_snake - 1)
        pygame.display.update()
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, W - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, H - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()


game_loop()
