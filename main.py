import pygame
from setings import *


WIDTH, HEIGHT = 1080, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mugman")
WHITE = (255,255,255)

class Game():
    
    def __init__(self):
        self.WIDTH = 1080
        self.HEIGHT = 600
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    def play(self):
        pygame.init()
        run = True
        while run == True: 
            self.screen.fill(WHITE)
            pygame.display.set_mode((self.WIDTH, self.HEIGHT))

