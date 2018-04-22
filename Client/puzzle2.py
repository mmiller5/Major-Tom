import string
import random
import pygame
from button import *

class Puzzle2(object):
    # load all possible button images
    # modified from Lucas Peraza's Asteroid.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    @staticmethod
    def init():
        image = pygame.image.load('images/checkers.png').convert_alpha()
        rows = 2
        cols = 2
        width, height = image.get_size()
        cellW = width / cols
        cellH = height / rows
        Puzzle2.checkers = dict()
        count = 0
        for tile in range(rows * cols):
            row = count // cols
            col = count % cols
            subImage = image.subsurface((col * cellW, row * cellH, cellW, cellH))
            Puzzle2.checkers[tile] = subImage
            count += 1
        image = pygame.image.load('images/highlight.png').convert_alpha()
        Puzzle2.highlight = image
    
    def __init__(self):#, firstMove):
        self.board = self.makeBoard()
        #makeMove(firstMove)
        self.x = 200
        self.y = 200
        self.tileSize = 30
        tiles = self.makeTiles()
        self.tiles = pygame.sprite.Group()
        for tile in tiles:
            self.tiles.add(tile)
        self.highlight = pygame.sprite.GroupSingle()
        self.clickedTile = None
    
    def makeBoard(self):
        board = [ 
                  ["W","0","W","0","W","0","W","0"],
                  ["0","1","0","1","0","1","0","1"],
                  ["1","0","1","0","1","0","1","0"],
                  ["0","1","0","1","0","1","0","1"],
                  ["1","0","1","0","1","0","1","0"],
                  ["0","1","0","1","0","1","0","1"],
                  ["1","0","1","0","1","0","1","0"],
                  ["0","B","0","B","0","B","0","B"]
                ]
        return board
    
    def makeMove(self, move):
        board = self.board
        row = move[0]
        col = move[1]
        newRow = move[2]
        newCol = move[3]
        isJump = move[4]
        #board[row][col], board[newRow][newCol] = "1", board[row][col]
        for tile in self.tiles:
            if tile.x == col and \
               tile.y == row:
                tile1 = tile
            elif tile.x == newCol and \
                 tile.y == newRow:
                tile2 = tile
        tile1.x, tile2.x = tile2.x, tile1.x
        tile1.y, tile2.y = tile2.y, tile1.y
        if isJump:
            jumpedRow = move[5]
            jumpedCol = move[6]
            for tile in self.tiles:
                if tile.x == jumpedCol and \
                tile.y == jumpedRow:
                    tile3 = tile
            tile3.image = pygame.transform.scale(Puzzle2.checkers[1],
                                                  (self.tileSize, self.tileSize))
    
    def makeTiles(self):
        tiles = []
        tileCount = 64
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
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
    
    def tileClick(self, x, y):
        for tile in self.tiles:
            if tile.rect.collidepoint(x, y):
                if self.clickedTile == None or \
                   self.clickedTile == tile:
                    self.clickedTile = tile
                else:
                    tile1 = self.clickedTile
                    tile2 = tile
                    # placeholder movement
                    move = [tile1.y, tile1.x, tile2.y, tile2.x, False]
                    self.makeMove(move)
                    self.clickedTile = None
    
    def update(self):
        self.tiles.update()
    
    def draw(self, screen):
        self.tiles.draw(screen)
        self.highlight.draw(screen)

class Button2(Button):
    def __init__(self, x, y, image):
        super(Button2, self).__init__(x, y, image)
        self.isClicked = False
    
    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x - w / 2, self.y - h / 2, w, h)
    
    def update(self):
        self.updateRect()
    
class Highlight(pygame.sprite.Sprite):
    def init(self, x, y, image):
        super(Highlight, self).__init__()
        
        
        
        
        
        
        
        
        