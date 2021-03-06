# contains image for backgrounds

import pygame
 
class Background(pygame.sprite.Sprite):
    @staticmethod
    def init():
        Background.MTimage = pygame.image.load('images/MTBackground.png').convert_alpha()
        Background.GCimage = pygame.image.load('images/GCBackground.png').convert_alpha()
        Background.StartImage = pygame.image.load('images/startMenu.png').convert_alpha()
        Background.WonImage = pygame.image.load('images/successScreen.png').convert_alpha()
        # next image modified from https://www.theflatearthsociety.org/forum/index.php?topic=62345.0
        Background.LostImage = pygame.image.load('images/failScreen.png').convert_alpha()
    
    def __init__(self, x, y, image):
        super(Background, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.baseImage = image.copy()
        self.rect = self.image.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y