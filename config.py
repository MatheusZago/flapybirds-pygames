import os

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800

#Pegando onde está as imagens
BASE_DIR = os.path.dirname(__file__)  # Diretório do script atual
BACKGROUND_IMAGE_PATH = os.path.join(BASE_DIR, 'assets', 'sprites', 'background-day.png')
BIRD_MID_IMAGE = os.path.join(BASE_DIR, 'assets', 'sprites', 'bluebird-midflap.png')