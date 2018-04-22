# Alpha-Beta Minimax code written by Eric Clinch
# https://drive.google.com/drive/folders/1lLCArvni4VB6sL6wTP3qZv-B8_lX2kxX
# modified by me

# takes a board, depth, alpha, and beta where alpha and beta are 
# the best scores guaranteed for Maxie and Minnie, respectively.0, 
# Returns a tuple (move, score) where move is the
# best move for Maxie and score is the board score that results
# from making that move. The best move is the one that maximizes
# Maxie's score by maximizing the board score.
# Uses alpha-beta pruning to prune this part of the game tree if it
# detects that this branch will never be relevant to the overall search.
# If depth is the max depth, returns the score given by a heuristic function
alpha = 0
beta = 0
maxDepth = 5
'''
def MaxieMoveWithHeuristics(board, depth, alpha, beta):
    if board.gameOver:
        return (None, 100) if board.won(Maxie) else (None, -100)
    elif depth == 0:
        return (None, board.heuristic(board))
    else:
        bestMove = None
        bestScore = -100
        for move in board.legalMoves("Maxie"):
            board.makeMove(move, "Maxie")
            _, moveScore = MinnieMoveWithHeuristics(board, depth - 1)
            board.undoMove(move, "Maxie")
            if moveScore > bestScore:
                bestScore = moveScore
                bestMove = move
                alpha = max(alpha, bestScore)
                if (alpha >= beta):
                    return (bestMove, bestScore)
        return (bestMove, bestScore)

# same as Maxie, but maximizes Minnie's score by minimizing
# the board score
def MinnieMoveWithHeuristics(board, depth, alpha, beta):
    if board.gameOver:
        return (None, -100) if board.won(Minnie) else (None, 100)
    elif depth == 0:
        return (None, board.heuristic(board))
    else:
        bestMove = None
        bestScore = 100
        for move in board.legalMoves("Minnie"):
            board.makeMove(move, "Minnie")
            _, moveScore = MaxieMoveWithHeuristics(board, depth - 1)
            board.undoMove(move, "Minnie")
            if moveScore < bestScore:
                bestScore = moveScore
                bestMove = move
                beta = min(beta, bestScore)
                if (alpha >= beta):
                    return (bestMove, bestScore)
        return (bestMove, bestScore)
'''
def MaxieMoveAlphaBeta(board, depth, alpha, beta):
    #assert(alpha < beta)
    if board.gameOver:
        return (None, 100) if board.won("Maxie") else (None, -100)
    elif depth == 0:
        return (None, board.heuristic(board))
    else:
        bestMove = None
        bestScore = -100
        for move in board.legalMoves("Maxie"):
            board.makeMove(move, "Maxie")
            moveScore = MinnieMoveAlphaBeta(board, depth - 1, alpha, beta)[1]
            board.undoMove(move, "Maxie")
            if moveScore > bestScore:
                bestScore = moveScore
                bestMove = move
                alpha = max(alpha, bestScore)
                if (alpha >= beta):
                    return (bestMove, bestScore)
        return (bestMove, bestScore)

# same as Maxie, but maximizes Minnie's score by minimizing
# the board score
def MinnieMoveAlphaBeta(board, depth, alpha, beta):
    #assert(alpha < beta)
    if board.gameOver:
        return (None, -100) if board.won("Minnie") else (None, 100)
    elif depth == 0:
        return (None, board.heuristic(board))
    else:
        bestMove = None
        bestScore = 100
        for move in board.legalMoves("Minnie"):
            board.makeMove(move, "Minnie")
            moveScore = MaxieMoveAlphaBeta(board, depth - 1, alpha, beta)[1]
            board.undoMove(move, "Minnie")
            if moveScore < bestScore:
                bestScore = moveScore
                bestMove = move
                beta = min(beta, bestScore)
                if (alpha >= beta):
                    return (bestMove, bestScore)
        return (bestMove, bestScore)
        
class Board(object):
    def init():
        # load images
        pass

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.whiteLeft = 4
        self.blackLeft = 4
        self.board = self.makeBoard()
        self.gameOver = False
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
    
    def legalMoves(self, player):
        moves = []
        board = self.board
        if player == "Minnie":
            for row in range(len(board) - 1):
                for col in range(len(board[row])):
                    if board[row][col] == "W":
                        print("found a white piece")
                        print(row, col)
                        if col - 1 >= 0 and \
                           board[row + 1][col - 1] == "1":
                            moves += [(row, col, row + 1, col - 1, False)]
                        if col + 1 < len(board[row]) and \
                           board[row + 1][col + 1] == "1":
                            moves += [(row, col, row + 1, col + 1, False)]
                        if col - 2 >= 0 and \
                           row + 2 <= len(board) and \
                           board[row + 1][col - 1] == "B" and \
                           board[row + 2][col - 2] == "1":
                            moves += [(row, col, row + 2, col - 2, True, row + 1, col - 1)]
                        if col + 2 < len(board[row]) and \
                           row + 2 < len(board) and \
                           board[row + 1][col + 1] == "B" and \
                           board[row + 2][col + 2] == "1":
                            moves += [(row, col, row + 2, col + 2, True, row + 1, col + 1)]
        if player == "Maxie":
            for row in range(1, len(board)):
                for col in range(len(board[row])):
                    if board[row][col] == "B":
                        print("found a black piece")
                        print(row, col)
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
                            moves += [(row, col, row - 2, col - 2, True, row - 1, col - 1)]
                        if col + 2 < len(board[row]) and \
                           row - 2 >= 0 and \
                           board[row - 1][col + 1] == "W" and \
                           board[row - 2][col + 2] == "1":
                            moves += [(row, col, row - 2, col + 2, True, row - 1, col + 1)]
        print(moves)
        return moves
        
    def makeMove(self, move, player):
        board = self.board
        row = move[0]
        col = move[1]
        newRow = move[2]
        newCol = move[3]
        isJump = move[4]
        board[row][col], board[newRow][newCol] = "1", board[row][col]
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
        board[oldRow][oldCol], board[row][col] = "1", board[oldRow][oldCol]
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
            score += (4 - i)
        for i in range(self.blackLeft):
            score -= (4 - i)
        return score
    
    def isLegalMove(self, move):
        board = self.board
        # assume starting position is legal
        move[0] = row
        move[1] = col
        move[2] = newRow
        move[3] = newCol
        if row - newRow == 1 and \
           abs(col - newCol) == 1 and \
           board[newRow][newCol] == "1":
            board[row][col], board[newRow][newCol] = "1", "B"
            return True
        elif row - newRow == 2 and \
             abs(col - newCol) == 2 and \
             board[newRow][newCol] == "1":
            jumpedRow = (newRow + row) / 2
            jumpedCol = (newCol + col) / 2
            if board[jumpedRow][jumpedCol] == "W":
                board[row][col], board[newRow][newCol] = "1", "B"
                board[jumpedRow][jumpedCol] = "1"
                return True
        return False
    
gameBoard = Board(0, 0)
    
    
    
    
    
    
    
    
    
    
    