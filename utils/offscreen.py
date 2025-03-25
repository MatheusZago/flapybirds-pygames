import pygame

def is_off_screen(sprite):
    #Ta vndo se o sprite ta inteiramente fora da tela (totalmente com coordenada negativa)
    return sprite.rect[0] < -(sprite.rect[2])
