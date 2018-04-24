# Specific class for what Ground Control receives of the checkers puzzle

from puzzle2 import *

class Puzzle2GC(Puzzle2):    
    def __init__(self):
        super().__init__()
        self.highlightImage = pygame.transform.scale(Puzzle2.highlight,
                                                  (self.tileSize, self.tileSize))
        self.highlight = pygame.sprite.GroupSingle()
        timer = Timer(315, 303, Timer.image, 3000)
        self.timer = pygame.sprite.GroupSingle(timer)
        
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
                    highlight = Highlight(tile.x, tile.y, self.highlightImage)
                    self.highlight.add(highlight)
                    return None
                elif self.clickedTile == tile:
                    self.clickedTile = None
                    self.highlight.sprite.kill()
                    return None
                else:
                    tile1 = self.clickedTile
                    tile2 = tile
                    self.clickedTile = None
                    self.highlight.sprite.kill()
                    return (tile1.row, tile1.col, tile2.row, tile2.col)
    
    def draw(self, screen):
        self.tiles.draw(screen)
        self.highlight.draw(screen)
        self.timer.draw(screen)

class Highlight(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super(Highlight, self).__init__()
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