import sys
import pygame
from pygame.locals import KEYDOWN, QUIT, K_ESCAPE, K_UP

from static_variables import SCREEN_WIDTH, SCREEN_HIGHT, GAME_IMAGES, SCREEN, fps_clock, ground_y, FPS


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
            if event.type == QUIT and event.type == pygame.KEYDOWN:
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
