import pygame
from pygame.locals import *
import sys
from welcome_page import welcome_screen

from static_variables import fps_clock, FPS, SCREEN_WIDTH, SCREEN_HIGHT, GAME_SOUNDS, GAME_IMAGES, ground_y, SCREEN
from utils import get_random_pipe, is_collide

fps_clock.tick(FPS)


def main_game():
    score = 0
    player_x = (SCREEN_WIDTH/8)
    player_y = (SCREEN_HIGHT/2)
    base_x = 0

    new_pipe1 = get_random_pipe()
    new_pipe2 = get_random_pipe()

    upper_pipes = [
        {'x': SCREEN_WIDTH+200, 'y': new_pipe1[0]['y']},
        {'x': SCREEN_WIDTH+200+(SCREEN_WIDTH/2), 'y': new_pipe2[0]['y']}
    ]

    lower_pipes = [
        {'x': SCREEN_WIDTH+200, 'y': new_pipe1[1]['y']},
        {'x': SCREEN_WIDTH+200+(SCREEN_WIDTH/2), 'y': new_pipe2[1]['y']}
    ]

    pipe_vel_x = -4

    player_vel_y = -9
    player_max_vel_y = 10
    player_acc_y = 1

    player_flap_vel = -8
    player_flapped = False

    while True:
        for event in pygame.event.get():
            if event.type == K_DOWN or event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if player_y > 0:
                    player_vel_y = player_flap_vel
                    player_flapped = True
                    GAME_SOUNDS['wing'].play()

        # if player hit border or pipe return
        crash_test = is_collide(player_x, player_y, upper_pipes, lower_pipes)
        if crash_test:
            return

        player_mid_pos = player_x + GAME_IMAGES['player'].get_width()/2
        for pipe in upper_pipes:
            pipe_mid_pos = pipe['x'] + GAME_IMAGES['pipe'][0].get_width()/2
            if pipe_mid_pos <= player_mid_pos < pipe_mid_pos + 4:
                score += 1
                print(f"Your Score is {score}")
                GAME_SOUNDS['point'].play()

        if player_vel_y < player_max_vel_y and not player_flapped:
            player_vel_y += player_acc_y

        if player_flapped:
            player_flapped = False
        player_height = GAME_IMAGES['player'].get_height()
        player_y = player_y + \
            min(player_vel_y, ground_y - player_y - player_height)

        for upper_pipe, lower_pipe in zip(upper_pipes, lower_pipes):
            upper_pipe['x'] += pipe_vel_x
            lower_pipe['x'] += pipe_vel_x

        if 0 < upper_pipes[0]['x'] < 5:
            new_pipe = get_random_pipe()
            upper_pipes.append(new_pipe[0])
            lower_pipes.append(new_pipe[1])

        if upper_pipes[0]['x'] < -GAME_IMAGES['pipe'][0].get_width():
            upper_pipes.pop(0)
            lower_pipes.pop(0)

        SCREEN.blit(GAME_IMAGES['background'], (0, 0))
        for upper_pipe, lower_pipe in zip(upper_pipes, lower_pipes):
            SCREEN.blit(GAME_IMAGES['pipe'][0],
                        (upper_pipe['x'], upper_pipe['y']))
            SCREEN.blit(GAME_IMAGES['pipe'][1],
                        (lower_pipe['x'], lower_pipe['y']))
        SCREEN.blit(GAME_IMAGES['ground'], (base_x, ground_y))
        SCREEN.blit(GAME_IMAGES['player'], (player_x, player_y))

        my_digits = [int(x) for x in list(str(score))]
        width = 0
        for digit in my_digits:
            width += GAME_IMAGES['numbers'][digit].get_width()
        x_offset = (SCREEN_WIDTH - width)/2

        for digit in my_digits:
            SCREEN.blit(GAME_IMAGES['numbers'][digit],
                        (x_offset, SCREEN_HIGHT*0.12))
            x_offset += GAME_IMAGES['numbers'][digit].get_width()
        pygame.display.update()
        fps_clock.tick(FPS)


if __name__ == "__main__":
    while True:
        welcome_screen()
        main_game()
