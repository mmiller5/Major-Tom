import pygame
import math
from GameObject import GameObject


class Dino(GameObject):
    @staticmethod
    def init():
        Dino.dinoImage = pygame.transform.scale(
            pygame.image.load('images/dino.png').convert_alpha(),
            (50, 50))
    
    def __init__(self, x, y):
        super(Dino, self).__init__(x, y, Dino.dinoImage, 25)