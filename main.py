import pygame
from pygame.locals import *
import Config
import Bird
from Ground import Ground

pygame.init()
screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))

BACKGROUND = pygame.image.load(Config.BACKGROUND_IMAGE_PATH)
BACKGROUND = pygame.transform.scale(BACKGROUND, (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))

bird_group = pygame.sprite.Group()
bird_instance = Bird.Bird()
bird_group.add(bird_instance)

ground_group = pygame.sprite.Group()
ground_instance = Ground(2 * Config.SCREEN_WIDTH, 100)
ground_group.add(ground_instance)

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
    ground_group.update()

    bird_group.draw(screen) #Desenha todos os elementos do grupo na tela
    ground_group.draw(screen)

    #Depois de cada laço ele atualiza pra mudar oq precisa ser mudado
    pygame.display.update()