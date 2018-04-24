# Specific class for what Ground Control receives of the scanner puzzle

from puzzle1 import *
from button import *


class Puzzle1GC(Puzzle1):
    def __init__(self, solution):
        self.solution = solution
        self.buttonLeft = 625
        self.buttonSize = 39
        self.buttonTop = 269
        self.buttonSpace = 5
        self.buttonLetters = set()
        self.buttons = pygame.sprite.Group()
        buttons = self.makeButtons()
        for button in buttons:
            self.buttons.add(button)
        timer = Timer(606, 309, Timer.image, 1000)
        self.timer = pygame.sprite.GroupSingle(timer)
    
    def makeButtons(self):
        buttons = []
        buttonCount = 4
        solutionPos = random.randint(0, buttonCount - 1)        
        self.buttonLetters.add(self.solution)
        for button in range(0, buttonCount):
            x = self.buttonLeft + (button * (self.buttonSize + self.buttonSpace))
            y = self.buttonTop
            if button == solutionPos:
                image = pygame.transform.scale(Puzzle1GC.answers[self.solution],
                                               (40, 40))
                buttons.append(Button1(x, y, image, True))
            else:
                answer = self.chooseAnswer()
                image = pygame.transform.scale(Puzzle1GC.answers[answer],
                                               (40, 40))
                buttons.append(Button1(x, y, image, False))
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
        self.timer.draw(screen)

class Button1(Button):
    def __init__(self, x, y, image, isSolution):
        super(Button1, self).__init__(x, y, image)
        self.isSolution = isSolution