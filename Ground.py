import pygame
import Config

class Ground(pygame.sprite.Sprite):

    def __init__(self, xposition):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(Config.BASE_IMAGE)
        self.image = pygame.transform.scale(self.image, (Config.GROUND_WIDTH, Config.GROUND_HEIGHT))

        self.rect = self.image.get_rect()
        self.rect[0] = xposition
        self.rect[1] = Config.SCREEN_HEIGHT - Config.GROUND_HEIGHT

    def update(self):
        self.rect[0] -=Config.GAME_SPEED
