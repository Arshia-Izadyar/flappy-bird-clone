import pygame
import random
from pygame.locals import *
import sys

FPS = 32
SCREEN_WIDTH = 288
SCREEN_HIGHT = 512
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
ground_y = SCREEN_HIGHT * 0.8
GAME_IMAGES = {}
GAME_SOUNDS = {}

# SCREEN_WIDTH

PLAYER = "asset/bluebird-upflap.png"
BACK_GROUND = "asset/background-day.png"
PIPE = "asset/pipe-red.png"
TITLE = "asset/message.png"
fps_clock = pygame.time.Clock()
pygame.init()


pygame.display.set_caption("Flappy Bird v2.0")
GAME_IMAGES["numbers"] = (
    pygame.image.load(
        "asset/0.png"
    ).convert_alpha(),
    pygame.image.load(
        "asset/1.png"
    ).convert_alpha(),
    pygame.image.load(
        "asset/2.png"
    ).convert_alpha(),
    pygame.image.load(
        "asset/3.png"
    ).convert_alpha(),
    pygame.image.load(
        "asset/4.png"
    ).convert_alpha(),
    pygame.image.load(
        "asset/5.png"
    ).convert_alpha(),
    pygame.image.load(
        "asset/6.png"
    ).convert_alpha(),
    pygame.image.load(
        "asset/7.png"
    ).convert_alpha(),
    pygame.image.load(
        "asset/8.png"
    ).convert_alpha(),
    pygame.image.load(
        "asset/0.png"
    ).convert_alpha()
)
GAME_IMAGES["player"] = pygame.image.load(PLAYER).convert_alpha()
GAME_IMAGES["background"] = pygame.image.load(BACK_GROUND).convert_alpha()
GAME_IMAGES["pipe"] = (
    pygame.image.load(PIPE).convert_alpha(),
    pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha(), 180)
)
GAME_IMAGES["title"] = pygame.image.load(TITLE).convert_alpha()
GAME_IMAGES["ground"] = pygame.image.load(
    "D:/Code/flappy/flappy-bird-assets-master/sprites/base.png"
).convert_alpha()
GAME_IMAGES["message"] = pygame.image.load(
    "D:/Code/flappy/flappy-bird-assets-master/sprites/gameover.png"
).convert_alpha()

# add sounds

GAME_SOUNDS["hit"] = pygame.mixer.Sound(
    "D:/Code/flappy/flappy-bird-assets-master/audio/hit.wav")
GAME_SOUNDS["die"] = pygame.mixer.Sound(
    "D:/Code/flappy/flappy-bird-assets-master/audio/die.wav")
GAME_SOUNDS["point"] = pygame.mixer.Sound(
    "D:/Code/flappy/flappy-bird-assets-master/audio/point.wav")
GAME_SOUNDS["swoosh"] = pygame.mixer.Sound(
    "D:/Code/flappy/flappy-bird-assets-master/audio/swoosh.wav")
GAME_SOUNDS["wing"] = pygame.mixer.Sound(
    "D:/Code/flappy/flappy-bird-assets-master/audio/wing.wav")


def welcome_screen():
    player_x = int(SCREEN_WIDTH/8)
    player_y = int((SCREEN_HIGHT - GAME_IMAGES['player'].get_height())/2)

    message_x = int((SCREEN_WIDTH - GAME_IMAGES["message"].get_width()))
    message_y = int(SCREEN_HIGHT*0.2)
    title_x = int((SCREEN_WIDTH - GAME_IMAGES["title"].get_width())/2)
    title_y = int(SCREEN_HIGHT*0.04)
    base_x = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT and event.type() == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_UP):
                return
            else:
                SCREEN.blit(GAME_IMAGES["background"], (0, 0))
                SCREEN.blit(GAME_IMAGES["title"], (title_x, title_y))
                SCREEN.blit(GAME_IMAGES["player"], (player_x, player_y))
                # SCREEN.blit(GAME_IMAGES["message"], (message_x, message_y))
                SCREEN.blit(GAME_IMAGES["ground"], (base_x, ground_y))
                pygame.display.update()
                fps_clock.tick(FPS)


def main_game():
    score = 0
    player_x = (SCREEN_WIDTH/8)
    player_y = (SCREEN_HIGHT/2)
    base_x = 0

    new_pipe1 = get_random_pipe()
    new_pipe2 = get_random_pipe()

    upperPipes = [
        {'x': SCREEN_WIDTH+200, 'y': new_pipe1[0]['y']},
        {'x': SCREEN_WIDTH+200+(SCREEN_WIDTH/2), 'y': new_pipe2[0]['y']}
    ]

    lowerPipes = [
        {'x': SCREEN_WIDTH+200, 'y': new_pipe1[1]['y']},
        {'x': SCREEN_WIDTH+200+(SCREEN_WIDTH/2), 'y': new_pipe2[1]['y']}
    ]

    pipeVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapVel = -8
    playerFlapped = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if player_y > 0:
                    playerVelY = playerFlapVel
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()

        crashTest = isCollide(player_x, player_y, upperPipes, lowerPipes)
        if crashTest:
            return

        playerMidPos = player_x + GAME_IMAGES['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_IMAGES['pipe'][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipeMidPos + 4:
                score += 1
                print(f"Your Score is {score}")
                GAME_SOUNDS['point'].play()

        if playerVelY < playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False
        playerHeight = GAME_IMAGES['player'].get_height()
        player_y = player_y + \
            min(playerVelY, ground_y - player_y - playerHeight)

        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        if 0 < upperPipes[0]['x'] < 5:
            newPipe = get_random_pipe()
            upperPipes.append(newPipe[0])
            lowerPipes.append(newPipe[1])

        if upperPipes[0]['x'] < -GAME_IMAGES['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)

        SCREEN.blit(GAME_IMAGES['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_IMAGES['pipe'][0],
                        (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_IMAGES['pipe'][1],
                        (lowerPipe['x'], lowerPipe['y']))
        SCREEN.blit(GAME_IMAGES['ground'], (base_x, ground_y))
        SCREEN.blit(GAME_IMAGES['player'], (player_x, player_y))

        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_IMAGES['numbers'][digit].get_width()
        Xoffset = (SCREEN_WIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_IMAGES['numbers'][digit],
                        (Xoffset, SCREEN_HIGHT*0.12))
            Xoffset += GAME_IMAGES['numbers'][digit].get_width()
        pygame.display.update()
        fps_clock.tick(FPS)


def isCollide(player_x, player_y, upperPipes, lowerPipes):
    if player_y > ground_y-25 or player_y < 0:
        GAME_SOUNDS['hit'].play()
        return True

    for pipe in upperPipes:
        pipeHeight = GAME_IMAGES['pipe'][0].get_height()
        if (player_y < pipeHeight + pipe['y']) and (abs(player_x - pipe['x']) < GAME_IMAGES['pipe'][0].get_width() - 15):
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if (player_y + GAME_IMAGES['player'].get_height() > pipe['y']) and (abs(player_x - pipe['x']) < GAME_IMAGES['pipe'][0].get_width() - 15):
            GAME_SOUNDS['hit'].play()

            return True

    return False


def get_random_pipe():
    pipeHeight = GAME_IMAGES['pipe'][0].get_height()
    offset = SCREEN_HIGHT/3
    y2 = offset + \
        random.randrange(
            0, int(SCREEN_HIGHT - GAME_IMAGES['ground'].get_height() - 1.2*offset))
    pipeX = SCREEN_WIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1},
        {'x': pipeX, 'y': y2}
    ]
    return pipe


if __name__ == "__main__":
    while True:
        welcome_screen()
        main_game()
