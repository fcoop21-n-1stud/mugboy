import pygame
from setings import *
from pygame import mixer


WIDTH, HEIGHT = 1900, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mugman")
WHITE = (255,255,255)
backround = pygame.image.load("newmenu.jpg")

class Game():
    
    def __init__(self):
        self.WIDTH = 1900
        self.HEIGHT = 1000
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("slowsun.mp3")
    pygame.mixer.music.play(-1)  
    def play(self):
        pygame.init()
        run = True
        while run == True: 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            self.screen.fill(WHITE)
            pygame.display.set_mode((self.WIDTH, self.HEIGHT))
            screen.blit(backround,(0,0)) 
            pygame.display.flip()
            self.clock.tick(60)
        self.pygame.quit()
        


running = Game()
running.play()