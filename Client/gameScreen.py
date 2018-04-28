# contains all the stuff for the gameplay

from mode import *
from background import *
from puzzle1GC import *
from puzzle1MT import *
from puzzle2GC import *
from puzzle2MT import *
import random
import pygame
from pygamegame import PygameGame

class GameMode(Mode):
    @staticmethod
    def init():
        Puzzle1.init()
        Puzzle2.init()
        #Puzzle3.init()
        Timer.init()

    def __init__(self, player):
        self.player = player
        self.solution = "Z"
        self.background = None
        if self.player == "GC":
            self.background = Background(0, 0, Background.GCimage)
            self.puzzle1 = Puzzle1GC(self.solution)
            self.puzzle2 = Puzzle2GC()
        else:
            self.background = Background(0, 0, Background.MTimage)
            self.puzzle1 = Puzzle1MT(self.solution)
            self.puzzle2 = Puzzle2MT()
    
    def mousePressed(self, x, y):
        if self.player == "GC":
            if True: # find dimensions later
                puzzle1Correct = self.puzzle1.buttonClick(x, y)
                if puzzle1Correct != None:
                    forServer = True
                    msg = "puzzle1Response %s %s\n" % (forServer, puzzle1Correct)
                    print ("sending: ", msg,)
                    return msg
            if self.puzzle2.x <= x <= self.puzzle2.x + 8 * self.puzzle2.tileSize and \
                self.puzzle2.y <= y <= self.puzzle2.y + 8 * self.puzzle2.tileSize:
                move = self.puzzle2.tileClick(x, y)
                if move != None:
                    forServer = True
                    row = move[0]
                    col = move[1]
                    newRow = move[2]
                    newCol = move[3]
                    msg = "puzzle2MoveMade %s %d %d %d %d\n" % (forServer, row, col, newRow, newCol)
                    print ("sending: ", msg,)
                    return msg
            elif self.puzzle2.highlight.sprite != None:
                self.puzzle2.clickedTile = None
                self.puzzle2.highlight.sprite.kill()
        else:
            pass
        return None
    
    def timerFired(self):
        if self.player == "GC":
            pass
        else:
            self.puzzle1.update()
        self.puzzle1.timer.update()
        self.puzzle2.timer.update()
        # check if puzzle failed
        if self.puzzle1.timer.sprite.timerDone() or \
            self.puzzle2.timer.sprite.timerDone():
            pass
    
    def draw(self, screen):
        screen.blit(self.background.image, self.background.rect)
        if self.puzzle1 != None:
            self.puzzle1.draw(screen)
        if self.puzzle2 != None:
            self.puzzle2.draw(screen)