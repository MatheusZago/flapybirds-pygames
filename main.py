import pygame
from pygame.locals import *
import Config
import Bird
from Ground import Ground
from utils.offscreen import is_off_screen
from Pipe import Pipe
from utils.GeneratePipes import get_random_pipes


pygame.init()
screen = pygame.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))

BACKGROUND = pygame.image.load(Config.BACKGROUND_IMAGE_PATH)
BACKGROUND = pygame.transform.scale(BACKGROUND, (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))

bird_group = pygame.sprite.Group()
bird_instance = Bird.Bird()
bird_group.add(bird_instance)

ground_group = pygame.sprite.Group()
for i in range(2):
    ground_instance = Ground(Config.GROUND_WIDTH * i)
    ground_group.add(ground_instance)

pipe_group = pygame.sprite.Group()
for i in range(2):
    pipes = get_random_pipes(Config.SCREEN_WIDTH * i + 600)
    pipe_group.add(pipes[0])
    pipe_group.add(pipes[1])

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

    if is_off_screen(ground_group.sprites()[0]):
        ground_group.remove(ground_group.sprites()[0])

        new_ground = Ground(Config.GROUND_WIDTH - 20)
        ground_group.add(new_ground)


    bird_group.update()
    ground_group.update()
    pipe_group.update()

    bird_group.draw(screen) #Desenha todos os elementos do grupo na tela
    ground_group.draw(screen)
    pipe_group.draw(screen)

    #Se os grupos colidirem com os pixeis não transparentes colidirem
    if pygame.sprite.groupcollide(bird_group, ground_group, False, False, pygame.sprite.collide_mask):
        #Game Ovr
        break

    #Depois de cada laço ele atualiza pra mudar oq precisa ser mudado
    pygame.display.update()

