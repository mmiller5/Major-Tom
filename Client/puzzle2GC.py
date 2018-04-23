# Specific class for what Ground Control receives of the checkers puzzle

from puzzle2 import *

class Puzzle2GC(Puzzle2):    
    def __init__(self):
        super().__init__()
        self.highlight = pygame.sprite.GroupSingle()

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
                elif self.board[row][col] == "1" or \
                     self.board[row][col] == "W":
                    image = pygame.transform.scale(Puzzle2.checkers[1],
                                                  (self.tileSize, self.tileSize))
                elif self.board[row][col] == "B":
                    image = pygame.transform.scale(Puzzle2.checkers[2],
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
                    return (tile1.row, tile1.col, tile2.row, tile2.col)
    
    def draw(self, screen):
        self.tiles.draw(screen)
        self.highlight.draw(screen)

class Highlight(pygame.sprite.Sprite):
    def init(self, x, y, image):
        super(Highlight, self).__init__()