from button1 import *
import string
import random
import pygame

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
        count = 0
        for letter in string.ascii_uppercase:
            row = count // cols
            col = count % cols
            subImage = image.subsurface((col * cellW, row * cellH, cellW, cellH))
            Puzzle1GC.answers[letter] = subImage
            count += 1
    
    def __init__(self, solution):
        self.solution = solution
        self.buttonLeft = 50
        self.buttonSize = 50
        self.buttonTop = 300
        self.buttonLetters = set()
        self.buttons = pygame.sprite.Group()
        buttons = self.makeButtons()
        for button in buttons:
            self.buttons.add(button)
        
    
    def makeButtons(self):
        buttons = []
        buttonCount = 4
        solutionPos = random.randint(0, buttonCount - 1)        
        self.buttonLetters.add(self.solution)
        for button in range(0, buttonCount):
            x = self.buttonLeft + (button * self.buttonSize)
            y = self.buttonTop
            if button == solutionPos:
                buttons.append(Button1(x, y, Puzzle1GC.answers[self.solution], True))
            else:
                answer = self.chooseAnswer()
                buttons.append(Button1(x, y, Puzzle1GC.answers[answer], False))
                self.buttonLetters.add(answer)
        return buttons
    
    def chooseAnswer(self):
        answer = self.solution
        while answer in self.buttonLetters:
            answer = random.choice(string.ascii_uppercase)
        return answer
    
    def buttonClick(self, x, y):
        for button in self.buttons:
            if button.rect.collidepoint(x, y):
                return button.isSolution
        return None

    def draw(self, screen):
        self.buttons.draw(screen)
    