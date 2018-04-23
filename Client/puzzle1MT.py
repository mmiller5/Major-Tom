# Specific class for what Major Tom receives of the scanner puzzle

from puzzle1 import Puzzle1

class Puzzle1MT(Puzzle1):
    
    def __init__(self, solution):
        self.solution = solution
        self.letterLeft = 660
        self.letterTop = 275
        self.letterImage = Puzzle1MT.answers[self.solution]
        self.presentedLetterImage = pygame.transform.scale(
                                    self.letterImage, (100, 100))
        letter = Letter(self.letterLeft, self.letterTop, self.presentedLetterImage)
        self.letterGroup = pygame.sprite.GroupSingle(letter)
        self.terminalImage = Puzzle1.MTTerminal
        terminal = Terminal(800, 600, self.terminalImage)
        self.terminalGroup = pygame.sprite.GroupSingle(terminal)

    def update(self):
        self.letterGroup.update()

    def draw(self, screen):
        self.letterGroup.draw(screen)
        self.terminalGroup.draw(screen)


class Letter(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Letter, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.top = self.y
        self.bottom = self.y + (1.25 * self.image.get_size()[1])
        self.dy = 3
        self.baseImage = image.copy()
        self.updateRect()

    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x - w / 2, self.y - h / 2, w, h)
    
    def update(self):
        self.y += self.dy
        if self.y >= self.bottom:
            self.y = self.top
        self.updateRect()

class Terminal(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Terminal, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.left = self.x
        self.rect.top = self.y
        self.updateRect()
    
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x - w, self.y - h, w, h)
        
        