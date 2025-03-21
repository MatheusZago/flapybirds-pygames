import pygame
from pygame.locals import *

#Tamanho da tela
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800


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

    #Depois de cada laço ele atualiza pra mudar oq precisa ser mudado
    pygame.display.update()