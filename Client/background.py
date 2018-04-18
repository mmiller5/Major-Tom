import pygame
 
class Background(pygame.sprite.Sprite):
    @staticmethod
    def init():
        Background.image = pygame.image.load('images/MTBackground.png').convert_alpha()
    
    def __init__(self, x, y, image):
        super(Background, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.baseImage = image.copy()
        self.rect = self.image.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y