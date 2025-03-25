import os

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800

SPEED = 10
GRAVITY = 0.7 
GAME_SPEED = 10

GROUND_WIDTH = 2 * SCREEN_WIDTH
GROUND_HEIGHT = 100

PIPE_WIDHT = 80
PIPE_HEIGHT = 500
PIPE_GAP = 200

#Pegando onde está as imagens
BASE_DIR = os.path.dirname(__file__)  # Diretório do script atual
BACKGROUND_IMAGE_PATH = os.path.join(BASE_DIR, 'assets', 'sprites', 'background-day.png')
BIRD_MID_IMAGE = os.path.join(BASE_DIR, 'assets', 'sprites', 'bluebird-midflap.png')
BIRD_UP_IMAGE = os.path.join(BASE_DIR, 'assets', 'sprites', 'bluebird-upflap.png')
BIRD_DOWN_IMAGE = os.path.join(BASE_DIR, 'assets', 'sprites', 'bluebird-downflap.png')
BASE_IMAGE = os.path.join(BASE_DIR, 'assets', 'sprites', 'base.png')
PIPE_IMAGE = os.path.join(BASE_DIR, 'assets', 'sprites', 'pipe-red.png')