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
        Button2.init(self.x, self.y, self.tileSize)
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
        row = int(move[0])
        col = int(move[1])
        newRow = int(move[2])
        newCol = int(move[3])
        if abs(row - newRow) == 2:
            isJump = True
        else:
            isJump = False
        for tile in self.tiles:
            if tile.col == col and \
               tile.row == row:
                tile1 = tile
            elif tile.col == newCol and \
                 tile.row == newRow:
                tile2 = tile
        tile1.col, tile2.col = tile2.col, tile1.col
        tile1.row, tile2.row = tile2.row, tile1.row
        if isJump:
            jumpedRow = int(move[5])
            jumpedCol = int(move[6])
            for tile in self.tiles:
                if tile.col == jumpedCol and \
                   tile.row == jumpedRow:
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
                if self.clickedTile == None:
                    self.clickedTile = tile
                    return None
                elif self.clickedTile == tile:
                    self.clickedTile = None
                    return None
                else:
                    tile1 = self.clickedTile
                    tile2 = tile
                    self.clickedTile = None
                    '''
                    row = (tile1.y - self.y) / self.tileSize
                    col = (tile1.x - self.x) / self.tileSize
                    newRow = (tile2.y - self.y) / self.tileSize
                    newCol = (tile2.x - self.x) / self.tileSize
                    '''
                    return (tile1.row, tile1.col, tile2.row, tile2.col)
                    '''
                    # placeholder movement
                    move = [tile1.y, tile1.x, tile2.y, tile2.x, False]
                    self.makeMove(move)
                    self.clickedTile = None
                    '''
    
    def update(self):
        self.tiles.update()
    
    def draw(self, screen):
        self.tiles.draw(screen)
        self.highlight.draw(screen)

class Button2(Button):
    def init(x, y, size):
        Button2.startx = x
        Button2.starty = y
        Button2.size = size
        
    def __init__(self, x, y, image):
        super(Button2, self).__init__(x, y, image)
        self.isClicked = False
        self.row = (self.y - Button2.starty) / Button2.size
        self.col = (self.x - Button2.startx) / Button2.size
    
    # taken from Lucas Peraza's GameObject.py,
    # https://github.com/LBPeraza/Pygame-Asteroids
    def updateRect(self):
        # update the object's rect attribute with the new x,y coordinates
        w, h = self.image.get_size()
        self.width, self.height = w, h
        self.rect = pygame.Rect(self.x - w / 2, self.y - h / 2, w, h)
    
    def update(self):
        self.x = Button2.startx + (self.col * Button2.size)
        self.y = Button2.starty + (self.row * Button2.size)
        self.updateRect()
    
class Highlight(pygame.sprite.Sprite):
    def init(self, x, y, image):
        super(Highlight, self).__init__()
        
        
        
        
        
        
        
        
        