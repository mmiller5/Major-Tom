#from puzzle1 import *
from button1 import *
import string
import random

class Puzzle1GC(object):
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
        Puzzle1GC.answers = dict()
        for letter in string.ascii_uppercase:
            row = letter // cols
            col = letter % cols
            subImage = image.subsurface((col * cell, row * cellH, cellW, cellH))
            Puzzle1GC.answers[key] = subImage
    
    def __init__(self, solution):
        self.solution = solution
        self.buttonLeft = 50
        self.buttonSize = 50
        self.buttonTop = 300
        self.buttons = self.makeButtons()
        self.buttonLetters = set()
    
    def makeButtons(self):
        # gonna need to modify later. currently solution is always first button
        buttons = []
        buttonCount = 4
        x = self.buttonLeft
        y = self.buttonTop
        buttons.append(Button1(x, y, Puzzle1GC.answers[self.solution], True))
        self.buttonLetters.add(self.solution)
        for button in range(1, buttonCount):
            x = self.buttonLeft + (button * self.buttonSize)
            y = self.buttonTop
            answer = self.chooseAnswer()
            buttons.append(Button1(x, y, Puzzle1GC.answers[answer], False))
            self.buttonLetters.add(answer)
        return buttons
    
    def chooseAnswer(self):
        answer = self.solution
        while not answer in self.buttonLetters:
            answer = random.choice(string.ascii_uppercase)
        return answer
    
    def draw(self, screen):
        for button in self.buttons:
            button.draw(screen)
    