import pygame
import Config

class Pipe(pygame.sprite.Sprite):

    def __init__(self, inverted, xposition, ysize):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(Config.PIPE_IMAGE).convert_alpha()
        self.image = pygame.transform.scale(self.image, (Config.PIPE_WIDHT, Config.PIPE_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect[0] = xposition

        if inverted:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect[1] = - (self.rect[3] - ysize)
        else: 
            self.rect[1] = Config.SCREEN_HEIGHT - ysize

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect[0] -= Config.GAME_SPEED