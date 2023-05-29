import random

from static_variables import GAME_SOUNDS, ground_y, GAME_IMAGES, SCREEN_HIGHT, SCREEN_WIDTH


def is_collide(player_x, player_y, upper_pipes, lower_pipes):
    if player_y > ground_y-25 or player_y < 0:
        GAME_SOUNDS['hit'].play()
        return True

    for pipe in upper_pipes:
        pipe_height = GAME_IMAGES['pipe'][0].get_height()
        if (player_y < pipe_height + pipe['y']) and (abs(player_x - pipe['x']) < GAME_IMAGES['pipe'][0].get_width() - 15):
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lower_pipes:
        if (player_y + GAME_IMAGES['player'].get_height() > pipe['y']) and (abs(player_x - pipe['x']) < GAME_IMAGES['pipe'][0].get_width() - 15):
            GAME_SOUNDS['hit'].play()

            return True

    return False


def get_random_pipe():
    pipe_height = GAME_IMAGES['pipe'][0].get_height()
    offset = SCREEN_HIGHT/3
    y2 = offset + \
        random.randrange(
            0, int(SCREEN_HIGHT - GAME_IMAGES['ground'].get_height() - 1.2*offset))
    pipe_x = SCREEN_WIDTH + 10
    y1 = pipe_height - y2 + offset
    pipe = [
        {'x': pipe_x, 'y': -y1},
        {'x': pipe_x, 'y': y2}
    ]
    return pipe
