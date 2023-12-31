import pygame

FPS = 32
SCREEN_WIDTH = 288
SCREEN_HIGHT = 512
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
ground_y = SCREEN_HIGHT * 0.8
GAME_IMAGES = {}
GAME_SOUNDS = {}


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
        "asset/9.png"
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
    "asset/base.png"
).convert_alpha()
GAME_IMAGES["message"] = pygame.image.load(
    "asset/gameover.png"
).convert_alpha()

# add sounds

GAME_SOUNDS["hit"] = pygame.mixer.Sound(
    "asset/hit.wav")
GAME_SOUNDS["die"] = pygame.mixer.Sound(
    "asset/die.wav")
GAME_SOUNDS["point"] = pygame.mixer.Sound(
    "asset/point.wav")
GAME_SOUNDS["swoosh"] = pygame.mixer.Sound(
    "asset/swoosh.wav")
GAME_SOUNDS["wing"] = pygame.mixer.Sound(
    "asset/wing.wav")
