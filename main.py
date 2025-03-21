import pygame
from pygame.locals import *
import config


pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))


BACKGROUND = pygame.image.load(config.BACKGROUND_IMAGE_PATH)
BACKGROUND = pygame.transform.scale(BACKGROUND, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

while True:
    #Evento é qualquer ação que pode realizar dentro do jogo
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.QUIT
            exit()

        #Colocando o background, ele começa no canto superior esquerto da
        screen.blit(BACKGROUND, (0, 0))

    #Depois de cada laço ele atualiza pra mudar oq precisa ser mudado
    pygame.display.update()