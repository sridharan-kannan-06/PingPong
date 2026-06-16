import pygame
import random

pygame.init()


WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")


direction = [0, 1]
angle = [0, 1, 2]

BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.6, 0.6

paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)
left_paddle_vel = right_paddle_vel = 0


left_gadget = right_gadget = 0
left_gadget_remaining = right_gadget_remaining = 5


run = True
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
            if i.key == pygame.K_RIGHT and right_gadget_remaining > 0:
                right_gadget = 1

            if i.key == pygame.K_w:
                left_paddle_vel = -0.9
            if i.key == pygame.K_s:
                left_paddle_vel = 0.9
            if i.key == pygame.K_d and left_gadget_remaining > 0:
                left_gadget = 1

        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0

    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= (-1)

    if ball_x >= WIDTH - radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if angle == 0:
                ball_vel_x, ball_vel_y = -1.2, 0.6
            if ang == 1:
                ball_vel_x, ball_vel_y = -0.6, 0.6
            if ang == 2:
                ball_vel_x, ball_vel_y = -0.6, 1.2
        if dir == 1:
            if angle == 0:
                ball_vel_x, ball_vel_y = 1.2, 0.6
            if ang == 1:
                ball_vel_x, ball_vel_y = 0.6, 0.6
            if ang == 2:
                ball_vel_x, ball_vel_y = 0.6, 1.2
        ball_vel_x *= (-1)

    if ball_x <= 0 + radius:
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        dir = random.choice(direction)
        ang = random.choice(angle)
        if dir == 0:
            if angle == 0:
                ball_vel_x, ball_vel_y = -1.2, 0.6
            if ang == 1:
                ball_vel_x, ball_vel_y = -0.6, 0.6
            if ang == 2:
                ball_vel_x, ball_vel_y = -0.6, 1.2
        if dir == 1:
            if angle == 0:
                ball_vel_x, ball_vel_y = 1.2, 0.6
            if ang == 1:
                ball_vel_x, ball_vel_y = 0.6, 0.6
            if ang == 2:
                ball_vel_x, ball_vel_y = 0.6, 1.2

    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0

    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= (-1)

    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= (-1)


    # SMASH
    if left_gadget == 1:
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                ball_vel_x *= (-2.5)
                left_gadget = 0
                left_gadget_remaining -= 1
    
    if right_gadget == 1:
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
            if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                ball_vel_x *= (-2.5)
                right_gadget = 0
                right_gadget_remaining -= 1

    ball_x += ball_vel_x
    ball_y += ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel
    
    pygame.draw.circle(wn, RED, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, BLUE, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, BLUE, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    if left_gadget == 1:
        pygame.draw.circle(wn, WHITE, (left_paddle_x + 10, left_paddle_y + 10), 4)
    if right_gadget == 1:
        pygame.draw.circle(wn, WHITE, (right_paddle_x + 10, right_paddle_y + 10), 4)
    pygame.display.update()