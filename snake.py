import pygame
import time
import random

pygame.init()

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)


# screen size
dis_width = 600
dis_height = 400

display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Python Snake')

clock = pygame.time.Clock()

block = 10
speed = 15

font_type = pygame.font.SysFont("arial", 25)
font_score = pygame.font.SysFont("arial", 25)


def your_score(score):
    value = font_score.render("Your Score: " + str(score), True, green)
    display.blit(value, [0, 0])


def snake(block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, white, [x[0], x[1], block, block])


def message(msg, color):
    mesg = font_type.render(msg, True, color)
    display.blit(mesg, [dis_width / 15, dis_height / 3])


def game_loop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, dis_width - block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display.fill(black)
            message("Game Over! Press \"A\" to play again or \"Q\" to quit", red)

            your_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_a:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(black)
        pygame.draw.rect(display, red, [foodx, foody, block, block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_list.append(snake_Head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_Head:
                game_close = True

        snake(block, snake_list)
        your_score(snake_length - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(
                0, dis_width - block) / 10.0) * 10.0
            foody = round(random.randrange(
                0, dis_height - block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(speed)

    pygame.quit()
    quit()


game_loop()
