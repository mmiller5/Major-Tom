# Specific class for what Major Tom receives of the tumbler

from puzzle3 import *

class Puzzle3MT(Puzzle3):
    def __init__(self, board):
        super().__init__(board)
        self.board = board
        timer = Timer(17, 424, Timer.image, 3000)
        self.timer = pygame.sprite.GroupSingle(timer)
        tumblers = self.makeTumblers()
        self.tumblers = pygame.sprite.Group()
        for tumbler in tumblers:
            self.tumblers.add(tumbler)
        arrows = self.makeArrows()
        self.arrows = pygame.sprite.Group()
        for arrow in arrows:
            self.arrows.add(arrow)
    
    def makeTumblers(self):
        tumblers = []
        tumblerCount = len(self.board)
        for i in range(tumblerCount):
            x = 41 + (24 * i)
            position = self.board[i][0]
            if position == "Up":
                y = 294
            else:
                y = 322
            number = self.board[i][1]
            image = Puzzle3.tumbler
            tumbler = Tumbler(x, y, image, position, number)
            tumblers.append(tumbler)
        return tumblers
    
    def makeArrows(self):
        arrows = []
        leftImage = Puzzle3.left
        leftArrow = Arrow(6, 294, leftImage, "Left")
        arrows.append(leftArrow)
        rightImage = Puzzle3.right
        rightArrow = Arrow(187, 294, rightImage, "Right")
        arrows.append(rightArrow)
        return arrows
    
    def mousePressed(self, x, y):
        for arrow in self.arrows:
            if arrow.rect.collidepoint(x, y):
                direction = arrow.direction
                print(direction)
    
    def draw(self, screen):
        self.tumblers.draw(screen)
        self.arrows.draw(screen)

class Tumbler(pygame.sprite.Sprite):
    def __init__(self, x, y, image, position, number):
        super(Tumbler, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.position = position
        self.number = number
        self.updateRect()
        
    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x, self.y, w, h)
    
    def move(self):
        if self.position == "Up":
            self.position = "Down"
            self.y = 322
        else:
            self.position = "Up"
            self.y = 294
        self.updateRect()

class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, image, direction):
        super(Arrow, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.direction = direction
        self.updateRect()
    
    def clicked():
        pass

    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x, self.y, w, h)