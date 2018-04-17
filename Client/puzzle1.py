import string
import random
import pygame

class Puzzle1(object):
    # load all possible button images
    # modified from Lucas Peraza's Asteroid.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    @staticmethod
    def init():
        image = pygame.image.load('images/letters.png').convert_alpha()
        rows = 4
        cols = 7
        width, height = image.get_size()
        cellW = width / cols
        cellH = height / rows
        Puzzle1.answers = dict()
        count = 0
        for letter in string.ascii_uppercase:
            row = count // cols
            col = count % cols
            subImage = image.subsurface((col * cellW, row * cellH, cellW, cellH))
            Puzzle1.answers[letter] = subImage
            count += 1

    def __init__(self, solution):
        self.solution = solution
    