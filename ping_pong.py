import pygame
import random

pygame.init()

# Window
WIDTH, HEIGHT = 1000, 600
wn = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Score
player_1 = player_2 = 0

# Randomise Ball Direction
direction = [0, 1]
angle = [0, 1, 2]

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ball
radius = 15
ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
ball_vel_x, ball_vel_y = 0.6, 0.6

# Paddle
paddle_width, paddle_height = 20, 120
left_paddle_y = right_paddle_y = HEIGHT/2 - paddle_height/2
left_paddle_x, right_paddle_x = 100 - paddle_width/2, WIDTH - (100 - paddle_width/2)
left_paddle_vel = right_paddle_vel = 0

# Powerups
left_gadget = right_gadget = 0
left_gadget_remaining = right_gadget_remaining = 5

run = True
while run:
    wn.fill(BLACK)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.KEYDOWN:
            # Right paddle, Player 2
            if i.key == pygame.K_UP:
                right_paddle_vel = -0.9
            if i.key == pygame.K_DOWN:
                right_paddle_vel = 0.9
            if i.key == pygame.K_RIGHT and right_gadget_remaining > 0:
                right_gadget = 1
            if i.key == pygame.K_LEFT and right_gadget_remaining > 0:
                right_gadget = 2
            # Left paddle, Player 1
            if i.key == pygame.K_w:
                left_paddle_vel = -0.9
            if i.key == pygame.K_s:
                left_paddle_vel = 0.9
            if i.key == pygame.K_d and left_gadget_remaining > 0:
                left_gadget = 1
            if i.key == pygame.K_a and left_gadget_remaining > 0:
                left_gadget = 2

        if i.type == pygame.KEYUP:
            right_paddle_vel = 0
            left_paddle_vel = 0

    # Bounce top and bottom walls
    if ball_y <= 0 + radius or ball_y >= HEIGHT - radius:
        ball_vel_y *= (-1)

    # Ball past right side
    if ball_x >= WIDTH - radius:
        player_1 += 1
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        # Random starting direction and angle
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

    # Ball past left side
    if ball_x <= 0 + radius:
        player_2 += 1
        ball_x, ball_y = WIDTH/2 - radius, HEIGHT/2 - radius
        # Random starting direction and angle
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

    # Paddles, keeps them inside screen
    if left_paddle_y >= HEIGHT - paddle_height:
        left_paddle_y = HEIGHT - paddle_height
    if left_paddle_y <= 0:
        left_paddle_y = 0
    if right_paddle_y >= HEIGHT - paddle_height:
        right_paddle_y = HEIGHT - paddle_height
    if right_paddle_y <= 0:
        right_paddle_y = 0

    # Paddle Collisions
    if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
        if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
            ball_x = left_paddle_x + paddle_width
            ball_vel_x *= (-1)

    if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
        if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
            ball_x = right_paddle_x
            ball_vel_x *= (-1)


    # POWER UPS
    # 1 - smash (right, d)
    # 2 - auto hit/track (left, a)
    if left_gadget == 1:
        if left_paddle_x <= ball_x <= left_paddle_x + paddle_width:
            if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
                ball_x = left_paddle_x + paddle_width
                ball_vel_x *= (-2.5)
                left_gadget = 0
                left_gadget_remaining -= 1
    elif left_gadget == 2:
        left_paddle_y = ball_y
        left_gadget = 0
        left_gadget_remaining -= 1
    
    if right_gadget == 1:
        if right_paddle_x <= ball_x <= right_paddle_x + paddle_width:
            if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
                ball_x = right_paddle_x
                ball_vel_x *= (-2.5)
                right_gadget = 0
                right_gadget_remaining -= 1
    elif right_gadget == 2:
        right_paddle_y = ball_y
        right_gadget = 0
        right_gadget_remaining -= 1

    # Update Ball Position
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    right_paddle_y += right_paddle_vel
    left_paddle_y += left_paddle_vel

    # Score and Powerup Text
    font = pygame.font.SysFont('callibri', 24)
    score_1 = font.render("Player 1: " + str(player_1), True, WHITE)
    wn.blit(score_1, (10, 10))
    score_2 = font.render("Player 2: " + str(player_2), True, WHITE)
    wn.blit(score_2, (795, 10))
    gad_left = font.render("Power-Ups Remaining: " + str(left_gadget_remaining), True, WHITE)
    wn.blit(gad_left, (10, 30))
    gad_right = font.render("Power-Ups Remaining: " + str(right_gadget_remaining), True, WHITE)
    wn.blit(gad_right, (795, 30))
    
    # Draw ball and paddles
    pygame.draw.circle(wn, RED, (ball_x, ball_y), radius)
    pygame.draw.rect(wn, BLUE, pygame.Rect(left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(wn, BLUE, pygame.Rect(right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    # Smash powerup indicator
    if left_gadget == 1:
        pygame.draw.circle(wn, WHITE, (left_paddle_x + 10, left_paddle_y + 10), 4)
    if right_gadget == 1:
        pygame.draw.circle(wn, WHITE, (right_paddle_x + 10, right_paddle_y + 10), 4)

    # Endscreen, Win Condition checking(first to 3)
    winning_font = pygame.font.SysFont('callibri', 100)
    if player_1 >= 3:
        wn.fill(BLACK)
        endscreen = winning_font.render("PLAYER 1 WON!!!", True, WHITE)
        wn.blit(endscreen, (200, 250))
    if player_2 >= 3:
        wn.fill(BLACK)
        endscreen = winning_font.render("PLAYER 2 WON!!!", True, WHITE)
        wn.blit(endscreen, (200, 250))

    pygame.display.update()