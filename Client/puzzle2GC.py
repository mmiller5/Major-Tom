import string
import random
import pygame
from puzzle2 import *
from button import *

class Puzzle2GC(Puzzle2):
    def __init__(self, firstMove):
        super().__init__(self, firstMove)
        self.tileSize = 30
        tiles = self.makeTiles()
        self.tiles = pygame.sprite.Group()
        for tile in tiles:
            self.tiles.add(tile)
    
    def makeTiles(self):
        tiles = []
        tileCount = 64
        for row in self.board:
            for col in row:
                x = self.x + (self.tileSize * col)
                y = self.y + (self.tileSize * row)
                if self.board[row][col] == "0":
                    image = pygame.transform.scale(Puzzle2.checkers[0],
                                                  (self.tileSize, self.tileSize))
                elif self.board[row][col] == "1":
                    image = pygame.transform.scale(Puzzle2.checkers[1],
                                                  (self.tileSize, self.tileSize))
                elif self.board[row][col] == "B":
                    image = pygame.transform.scale(Puzzle2.checkers[2],
                                                  (self.tileSize, self.tileSize))
                elif self.board[row][col] == "W":
                    image = pygame.transform.scale(Puzzle2.checkers[3],
                                                  (self.tileSize, self.tileSize))
                tile = Button2(x, y, image)
                tiles.append(tile)
        return tiles
    
    def draw(self, screen):
        self.tiles.draw(screen)
        
class Button2(Button):
    def __init__(self, x, y, image):
        super(Button2, self).__init__(x, y, image)