import pygame
import Config
import random
from Pipe import Pipe

def get_random_pipes(xposition):
    size = random.randint(100, 300)
    pipe = Pipe(False, xposition, size)
    pipe_inverted = Pipe(True, xposition, Config.SCREEN_HEIGHT - size - Config.PIPE_GAP)
    return (pipe, pipe_inverted)


