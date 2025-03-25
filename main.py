import pygame
from pygame.locals import *
import config
import bird

pygame.init()
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))


BACKGROUND = pygame.image.load(config.BACKGROUND_IMAGE_PATH)
BACKGROUND = pygame.transform.scale(BACKGROUND, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

bird_group = pygame.sprite.Group()
bird_instance = bird.Bird()
bird_group.add(bird_instance)

clock = pygame.time.Clock()

while True:
    clock.tick(30)
    #Evento é qualquer ação que pode realizar dentro do jogo
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if(event.key == K_SPACE):
                bird_instance.bump()

        #Colocando o background, ele começa no canto superior esquerto da
    screen.blit(BACKGROUND, (0, 0))

    bird_group.update()
    bird_group.draw(screen) #Desenha todos os elementos do grupo na tela

    #Depois de cada laço ele atualiza pra mudar oq precisa ser mudado
    pygame.display.update()