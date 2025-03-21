import pygame
from pygame.locals import *
import config

class Bird(pygame.sprite.Sprite):

    #Tem sempre que fazer esse método pra clkasse sprite fazer construções internamente de um sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #Todo sprite no pygame tem que ter uma imagem e rect, além de sobrescrever o método update
        self.image = pygame.image.load(config.BIRD_MID_IMAGE).convert_alpha() #isso é proa qnd tiver a transparencia (partes png)
        self.rect = self.image.get_rect() #diz onde está, tamanho e 
        print(self.rect)

    #Criando metodo de update placeholder
    def update(self):
        pass