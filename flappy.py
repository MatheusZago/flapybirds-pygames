import pygame
from pygame.locals import *
import os

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
#Pegando onde está as imagens
BASE_DIR = os.path.dirname(__file__)  # Diretório do script atual
BACKGROUND_IMAGE_PATH = os.path.join(BASE_DIR, 'assets', 'sprites', 'background-day.png')
BACKGROUND = pygame.image.load(BACKGROUND_IMAGE_PATH)
BACKGROUND = pygame.transform.scale(BACKGROUND, (SCREEN_WIDTH, SCREEN_HEIGHT))


#chamando a função de iniciar
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



while True:
    #Evento é qualquer ação que pode realizar dentro do jogo
    for event in pygame.event.get():
        #Se ele quiser sair ele chama a função de sair
        if event.type == QUIT:
            pygame.QUIT
            exit()

        #Colocando o background, ele começa no canto superior esquerto da
        screen.blit(BACKGROUND, (0, 0))

    #Depois de cada laço ele atualiza pra mudar oq precisa ser mudado
    pygame.display.update()