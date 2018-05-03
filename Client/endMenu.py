# end screen stuff

from mode import *
from button import *
from background import *
import pygame

class EndMode(Mode):
    @staticmethod
    def init():
        BackButton.init()
    
    def __init__(self, won):
        if won == "Won":
            self.background = Background(0, 0, Background.WonImage)
        else:
            self.background = Background(0, 0, Background.LostImage)
        self.makeBackButton()
    
    def makeBackButton(self):
        backButton = BackButton(250, 453)
        self.backButton = pygame.sprite.GroupSingle(backButton)
    
    def mousePressed(self, x, y):
        if self.backButton.sprite.rect.collidepoint(x, y):
            return self.backButton.sprite.clicked()
                
    def draw(self, screen):
        screen.blit(self.background.image, self.background.rect)
        self.backButton.draw(screen)

class BackButton(Button):
    @staticmethod
    def init():
        BackButton.backImage = pygame.image.load('images/backToStartButton.png').convert_alpha()
    
    def __init__(self, x, y):
        super(BackButton, self).__init__(x, y, BackButton.backImage)
        self.x = x
        self.y = y
        self.image = BackButton.backImage
        self.updateRect()
    
    def clicked(self):
        print("clicked back")
        return ("Back")
    
    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x, self.y, w, h)