# Specific class for what Major Tom receives of the tumbler

from puzzle3 import *
import copy

class Puzzle3MT(Puzzle3):
    def __init__(self, board):
        super().__init__(board)
        self.board = board
        #self.originalBoard = copy.deepcopy(self.board)
        timer = Timer(17, 424, Timer.image, 1700)
        self.timer = pygame.sprite.GroupSingle(timer)
        tumblers = self.makeTumblers()
        self.tumblers = pygame.sprite.Group()
        for tumbler in tumblers:
            self.tumblers.add(tumbler)
        arrows = self.makeArrows()
        self.arrows = pygame.sprite.Group()
        for arrow in arrows:
            self.arrows.add(arrow)
        self.makePlayer()
    
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
            tumbler = Tumbler(x, y, image, position, number, i)
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
    
    def makePlayer(self):
        image = Puzzle3.player
        player = Player(18, 334, image)
        self.player = pygame.sprite.GroupSingle(player)   
    
    def mousePressed(self, x, y):
        for arrow in self.arrows:
            if arrow.rect.collidepoint(x, y):
                direction = arrow.direction
                print(direction)
                return self.movePlayer(direction)
    
    def moveTumblers(self, number):
        for tumbler in self.tumblers:
            if number == tumbler.number:
                tumbler.move()
                location = tumbler.location
                position = tumbler.position
                self.board[location][0] = position
        self.checkCollision()
    
    def movePlayer(self, move):
        board = self.board
        if move == "Right":
            moveAmt = 1
        else:
            moveAmt = -1
        newLocation = max(-1, min(6, self.player.sprite.position + moveAmt))
        if newLocation == 6:
            self.player.sprite.move(newLocation)  
            return self.puzzle3Won()
        elif newLocation == -1 or board[newLocation][0] == "Up":
            self.player.sprite.move(newLocation)            
    
    def checkCollision(self):
        board = self.board
        position = self.player.sprite.position
        if 0 <= position < 6:
            if board[position][0] == "Down":
                self.puzzle3Reset()
    
    def puzzle3Won(self):
        print("won")
        return True
    
    def puzzle3Reset(self):
        print("dead")
        self.makePlayer()
    
    def draw(self, screen):
        self.tumblers.draw(screen)
        self.arrows.draw(screen)
        self.player.draw(screen)
        self.timer.draw(screen)

class Tumbler(pygame.sprite.Sprite):
    def __init__(self, x, y, image, position, number, location):
        super(Tumbler, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.position = position
        self.number = number
        self.location = location
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

    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x, self.y, w, h)

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Player, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.position = -1
        self.updateRect()
    
    def move(self, location):
        self.position = location
        self.x = 18 + (24 * (self.position + 1))
        self.updateRect()

    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x, self.y, w, h)