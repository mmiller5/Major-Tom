# Handles server-side checkerboard info and changes
        
class Board(object):
    def __init__(self):
        self.whiteLeft = 4
        self.blackLeft = 4
        self.board = self.makeBoard()
        self.won = None
    
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

    def isGameOver(self):
        if self.whiteLeft == 0:
            self.won = "Maxie"
            return True
        elif self.blackLeft == 0:
            self.won = "Minnie"
            return True
        return False
    
    def legalMoves(self, player):
        moves = []
        board = self.board
        if player == "Minnie":
            for row in range(len(board) - 1):
                for col in range(len(board[row])):
                    if board[row][col] == "W":
                        if col - 1 >= 0 and \
                           board[row + 1][col - 1] == "1":
                            moves += [(row, col, row + 1, col - 1, False)]
                        if col + 1 < len(board[row]) and \
                           board[row + 1][col + 1] == "1":
                            moves += [(row, col, row + 1, col + 1, False)]
                        if col - 2 >= 0 and \
                           row + 2 < len(board) and \
                           board[row + 1][col - 1] == "B" and \
                           board[row + 2][col - 2] == "1":
                            #print("jump move")
                            moves += [(row, col, row + 2, col - 2, True, row + 1, col - 1)]
                        if col + 2 < len(board[row]) and \
                           row + 2 < len(board) and \
                           board[row + 1][col + 1] == "B" and \
                           board[row + 2][col + 2] == "1":
                            #print("jump move")
                            moves += [(row, col, row + 2, col + 2, True, row + 1, col + 1)]
        if player == "Maxie":
            for row in range(1, len(board)):
                for col in range(len(board[row])):
                    if board[row][col] == "B":
                        if col - 1 >= 0 and \
                           board[row - 1][col - 1] == "1":
                            moves += [(row, col, row - 1, col - 1, False)]
                        if col + 1 < len(board[row]) and \
                           board[row - 1][col + 1] == "1":
                            moves += [(row, col, row - 1, col + 1, False)]
                        if col - 2 >= 0 and \
                           row - 2 >= 0 and \
                           board[row - 1][col - 1] == "W" and \
                           board[row - 2][col - 2] == "1":
                            #print("jump move")
                            moves += [(row, col, row - 2, col - 2, True, row - 1, col - 1)]
                        if col + 2 < len(board[row]) and \
                           row - 2 >= 0 and \
                           board[row - 1][col + 1] == "W" and \
                           board[row - 2][col + 2] == "1":
                            #print("jump move")
                            moves += [(row, col, row - 2, col + 2, True, row - 1, col + 1)]
        #print(moves)
        return moves

# makes move for AI
    def makeMove(self, move, player):
        board = self.board
        row = int(move[0])
        col = int(move[1])
        newRow = int(move[2])
        newCol = int(move[3])
        isJump = move[4]
        board[row][col], board[newRow][newCol] = board[newRow][newCol], board[row][col]
        if isJump:
            jumpedRow = move[5]
            jumpedCol = move[6]
            board[jumpedRow][jumpedCol] = "1"
            if player == "Minnie":
                self.blackLeft -= 1
            else:
                self.whiteLeft -= 1
    
    def undoMove(self, move, player):
        board = self.board
        oldRow = move[0]
        oldCol = move[1]
        row = move[2]
        col = move[3]
        wasJump = move[4]
        board[oldRow][oldCol], board[row][col] = board[row][col], board[oldRow][oldCol]
        if wasJump:
            jumpedRow = move[5]
            jumpedCol = move[6]
            if player == "Minnie":
                jumpedPiece = "B"
                self.blackLeft += 1
            else:
                jumpedPiece = "W"
                self.whiteLeft += 1
            board[jumpedRow][jumpedCol] = jumpedPiece
    
    def heuristic(self, board):
        score = 0
        for i in range(self.whiteLeft):
            score -= (4 - i)
        for i in range(self.blackLeft):
            score += (4 - i)
        return score
    
# checks if player move is legal, and makes move if it is
    def isLegalMove(self, move):
        board = self.board
        row = int(move[0])
        col = int(move[1])
        newRow = int(move[2])
        newCol = int(move[3])
        if board[row][col] != "B":
            return False
        if row - newRow == 1 and \
           abs(col - newCol) == 1 and \
           board[newRow][newCol] == "1":
            board[row][col], board[newRow][newCol] = "1", "B"
            return True
        elif row - newRow == 2 and \
             abs(col - newCol) == 2 and \
             board[newRow][newCol] == "1":
            jumpedRow = (newRow + row) // 2
            jumpedCol = (newCol + col) // 2
            if board[jumpedRow][jumpedCol] == "W":
                board[row][col], board[newRow][newCol] = "1", "B"
                board[jumpedRow][jumpedCol] = "1"
                self.whiteLeft -= 1
                return True
        return False
        
gameBoard = Board()
