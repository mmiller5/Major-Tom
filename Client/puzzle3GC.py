# Specific class for what Ground Control receives of the tumbler puzzle

from puzzle3 import *

class Puzzle3GC(Puzzle3):
    def __init__(self, board):
        super().__init__(board)
        self.board = board
        timer = Timer(25, 308, Timer.image, 3000)
        self.timer = pygame.sprite.GroupSingle(timer)
        numbers = self.makeNumbers()
        self.numbers = pygame.sprite.Group()
        for number in numbers:
            self.numbers.add(number)
        buttons = self.makeButtons()
        self.buttons = pygame.sprite.Group()
        for button in buttons:
            self.buttons.add(button)
    
    def makeNumbers(self):
        numbers = []
        numberCount = len(self.board)
        for i in range(numberCount):
            x = 8 + (34 * i)
            y = 213
            number = self.board[i][1]
            image = Puzzle3.numbers[number - 1]
            numberSprite = Number(x, y, image)
            numbers.append(numberSprite)
        return numbers

    def makeButtons(self):
        buttons = []
        for i in range(3):
            x = 21 + (i * 69)
            y = 258
            number = i
            image = Puzzle3.numButtons[number]
            button = NumButton(x, y, image, number + 1)
            buttons.append(button)
        return buttons

    def mousePressed(self, x, y):
        for button in self.buttons:
            if button.rect.collidepoint(x, y):
                number = arrow.number
                print(number)
    
    def draw(self, screen):
        self.numbers.draw(screen)
        self.buttons.draw(screen)
                
class Number(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Number, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.updateRect()
        
    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x, self.y, w, h)

class NumButton(pygame.sprite.Sprite):
    def __init__(self, x, y, image, number):
        super(NumButton, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.number = number
        self.updateRect()
        
    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x, self.y, w, h)