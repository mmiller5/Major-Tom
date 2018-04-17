from button1 import *
import string
import random
import pygame
from puzzle1 import Puzzle1

class Puzzle1MT(Puzzle1):
    def __init__(self, solution):
        self.solution = solution
        self.letterLeft = 50
        self.letterTop = 200
        self.letterImage = Puzzle1MT.answers[self.solution]
        self.presentedLetterImage = pygame.transform.scale(
                                    self.letterImage, (100, 100))
        letter = Letter(self.letterLeft, self.letterTop, self.presentedLetterImage)
        self.letterGroup = pygame.sprite.GroupSingle(letter)

    def draw(self, screen):
        self.letterGroup.draw(screen)


class Letter(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Letter, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.baseImage = image.copy()
        self.updateRect()

    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x - w / 2, self.y - h / 2, w, h)