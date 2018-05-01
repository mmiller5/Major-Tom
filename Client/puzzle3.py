# generic puzzle 3

import string
import random
import pygame
from timer import *
from button import *

class Puzzle3(object):
    # load all possible button images
    # modified from Lucas Peraza's Asteroid.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    @staticmethod
    def init():
        image = pygame.image.load('images/puzzle3Numbers.png').convert_alpha()
        rows = 1
        cols = 3
        width, height = image.get_size()
        cellW = width / cols
        cellH = height / rows
        Puzzle3.numbers = dict()
        count = 0
        for number in range(rows * cols):
            row = count // cols
            col = count % cols
            subImage = image.subsurface((col * cellW, row * cellH, cellW, cellH))
            Puzzle3.numbers[number] = subImage
            count += 1
        image = pygame.image.load('images/puzzle3NumButtons.png').convert_alpha()
        rows = 1
        cols = 3
        width, height = image.get_size()
        cellW = width / cols
        cellH = height / rows
        Puzzle3.numButtons = dict()
        count = 0
        for button in range(rows * cols):
            row = count // cols
            col = count % cols
            subImage = image.subsurface((col * cellW, row * cellH, cellW, cellH))
            Puzzle3.numButtons[button] = subImage
            count += 1
        Puzzle3.left = pygame.image.load('images/puzzle3Left.png').convert_alpha()
        Puzzle3.right = pygame.image.load('images/puzzle3Right.png').convert_alpha()
        Puzzle3.tumbler = pygame.image.load('images/puzzle3Tumbler.png').convert_alpha()
        #character image
    
    def __init__(self, board):
        self.board = board
    
    def draw(self, screen):
        pass