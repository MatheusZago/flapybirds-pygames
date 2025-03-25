import pygame
import Config

class Ground(pygame.sprite.Sprite):

    def __init__(self, widht, height):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(Config.BASE_IMAGE)
        self.image = pygame.transform.scale(self.image, (widht, height))

        self.rect = self.image.get_rect()
        self.rect[1] = Config.SCREEN_HEIGHT - height

    def update(self):
        self.rect[0] -=Config.GAME_SPEED
