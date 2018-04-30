# start screen stuff

from mode import *
from button import *
from background import *
import pygame

class StartMode(Mode):
    @staticmethod
    def init():
        StartButton.init()
        PlayerButton.init()
        PlayerTracker.init()
    
    def __init__(self, playerNum):
        self.playerNum = playerNum
        self.background = Background(0, 0, Background.StartImage)
        self.buttons = set()
        self.makePlayerButtons()
        self.makeStartButton()
        self.trackers = set()
        self.makePlayerTracker()
    
    def makePlayerButtons(self):
        gcImage = PlayerButton.GCButton
        gcButton = PlayerButton(501, 188, gcImage, "GC")
        self.GCButton = pygame.sprite.GroupSingle(gcButton)
        self.buttons.add(self.GCButton)
        mtImage = PlayerButton.MTButton
        mtButton = PlayerButton(501, 302, mtImage, "MT")
        self.MTButton = pygame.sprite.GroupSingle(mtButton)
        self.buttons.add(self.MTButton)
    
    def makeStartButton(self):
        startButton = StartButton(602, 416)
        self.startButton = pygame.sprite.GroupSingle(startButton)
        self.buttons.add(self.startButton)
    
    def makePlayerTracker(self):
        p1Image = PlayerTracker.p1Image
        p1Tracker = PlayerTracker(448, 214, p1Image, "p1")
        self.p1Tracker = pygame.sprite.GroupSingle(p1Tracker)
        self.trackers.add(self.p1Tracker)
        p2Image = PlayerTracker.p2Image
        p2Tracker = PlayerTracker(747, 326, p2Image, "p2")
        self.p2Tracker = pygame.sprite.GroupSingle(p2Tracker)
        self.trackers.add(self.p2Tracker)
    
    def timerFired(self):
        pass
    
    def mousePressed(self, x, y):
        for button in self.buttons:
            if button.sprite.rect.collidepoint(x, y):
                return button.sprite.clicked()
    
    def draw(self, screen):
        screen.blit(self.background.image, self.background.rect)
        for button in self.buttons:
            button.draw(screen)
        for tracker in self.trackers:
            tracker.draw(screen)





class StartButton(Button):
    @staticmethod
    def init():
        StartButton.startImage = pygame.image.load('images/StartButton.png').convert_alpha()
        StartButton.ready = pygame.image.load('images/ready.png').convert_alpha()
        StartButton.notReady = pygame.image.load('images/notReady.png').convert_alpha()
    
    def __init__(self, x, y):
        super(StartButton, self).__init__(x, y, StartButton.startImage)
        self.x = x
        self.y = y
        self.image = StartButton.startImage
        self.updateRect()
        self.isReady = True
    
    def clicked(self):
        if self.isReady:
            return ("Start")
    
    def findIsReady(self, player, otherPlayer):
        if player == otherPlayer:
            self.isReady = False
        else:
            self.isReady = True
    
    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x, self.y, w, h)






class PlayerButton(Button):
    @staticmethod
    def init():
        PlayerButton.GCButton = pygame.image.load('images/GCButton.png').convert_alpha()
        PlayerButton.MTButton = pygame.image.load('images/MTButton.png').convert_alpha()
    
    def __init__(self, x, y, image, player):
        super(PlayerButton, self).__init__(x, y, image)
        self.x = x
        self.y = y
        self.image = image
        self.player = player
        self.updateRect()
    
    def clicked(self):
        newPlayer = self.player
        return ("Player", newPlayer)

    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x, self.y, w, h)


class PlayerTracker(pygame.sprite.Sprite):
    @staticmethod
    def init():
        image1 = pygame.image.load('images/p1Button.png').convert_alpha()
        PlayerTracker.p1Image = image1
        image2 = pygame.image.load('images/p2Button.png').convert_alpha()
        PlayerTracker.p2Image = image2

    def __init__(self, x, y, image, playerNum):
        super(PlayerTracker, self).__init__()
        self.x = x
        self.y = y
        self.image = image
        self.playerNum = playerNum
        self.baseImage = image.copy()
        self.updateRect()
    
    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x, self.y, w, h)

    def move(self, player):
        if player == "GC":
            self.y = 214
        else:
            self.y = 326
        self.updateRect()
        
        
        
        
        