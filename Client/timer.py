# Generic timer class that counts down puzzles

import pygame

class Timer(pygame.sprite.Sprite):
    @staticmethod
    def init():
        image = pygame.image.load('images/timer.png').convert_alpha()
        Timer.image = image

    def __init__(self, x, y, image, totalTime):
        super(Timer, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.baseImage = image.copy()
        self.totalTime = totalTime
        self.startWidth, self.height = self.image.get_size()
        self.elapsedTime = 0
        self.updateRect()
    
    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x, self.y, w, h)

    def update(self):
        self.elapsedTime = min(self.elapsedTime + 1, self.totalTime)
        newWidth = max(int(self.startWidth * ((self.totalTime - self.elapsedTime) / self.totalTime)), 0)
        self.image = pygame.transform.scale(self.image, (newWidth, self.height))
        self.updateRect()
    
    def penalty(self, percent):
        amount = self.totalTime // (100 - percent)
        self.elapsedTime = min(self.elapsedTime + amount, self.totalTime)
    
    def reset(self):
        self.elapsedTime = 0