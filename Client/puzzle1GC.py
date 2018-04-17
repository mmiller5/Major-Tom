from button1 import *
import string
import random
import pygame
from puzzle1 import Puzzle1

class Puzzle1GC(Puzzle1):
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
    