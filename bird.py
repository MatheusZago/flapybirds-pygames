import pygame
from pygame.locals import *
import config

class Bird(pygame.sprite.Sprite):

    #Tem sempre que fazer esse método pra clkasse sprite fazer construções internamente de um sprite
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = [
            pygame.image.load(config.BIRD_UP_IMAGE).convert_alpha(),
            pygame.image.load(config.BIRD_MID_IMAGE).convert_alpha(),
            pygame.image.load(config.BIRD_DOWN_IMAGE).convert_alpha(),
        ]

        self.current_image = 1


        #Todo sprite no pygame tem que ter uma imagem e rect, além de sobrescrever o método update
        self.image = pygame.image.load(config.BIRD_UP_IMAGE).convert_alpha() #isso é proa qnd tiver a transparencia (partes png)
        self.rect = self.image.get_rect() #diz onde está, tamanho e 
        
        #Colocando o passaro na metade da tela
        self.rect.x = config.SCREEN_WIDTH/2
        self.rect.y = config.SCREEN_HEIGHT/2

        

    #Sempre que da update ele vai ciclar entre 1 e 3 para atualizar a imagem
    def update(self):
        # Atualiza a imagem para a próxima na lista, ciclando entre 0, 1, e 2
        self.current_image = (self.current_image + 1) % len(self.images)  # Garantir que o índice seja 0, 1 ou 2
        self.image = self.images[self.current_image]

