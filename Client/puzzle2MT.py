# Specific class for what Major Tom receives of the checkers puzzle

from puzzle2 import *

class Puzzle2MT(Puzzle2):   
    def __init__(self):
        super().__init__()
        timer = Timer(315, 300, Timer.image, 3000)
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
                     self.board[row][col] == "B":
                    image = pygame.transform.scale(Puzzle2.checkers[1],
                                                  (self.tileSize, self.tileSize))
                elif self.board[row][col] == "W":
                    image = pygame.transform.scale(Puzzle2.checkers[3],
                                                  (self.tileSize, self.tileSize))
                tile = Button2(x, y, image)
                tiles.append(tile)
        return tiles
    
    def draw(self, screen):
        self.tiles.draw(screen)
        self.timer.draw(screen)