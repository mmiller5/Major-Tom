# Alpha-Beta Minimax code written by Eric Clinch
# https://drive.google.com/drive/folders/1lLCArvni4VB6sL6wTP3qZv-B8_lX2kxX
# modified by me

#################################################################
# psuedocode for minimax with heuristics and alpha-beta pruning #
#################################################################

# takes a board, depth, alpha, and beta where alpha and beta are 
# the best scores guaranteed for Maxie and Minnie, respectively.
# Returns a tuple (move, score) where move is the
# best move for Maxie and score is the board score that results
# from making that move. The best move is the one that maximizes
# Maxie's score by maximizing the board score.
# Uses alpha-beta pruning to prune this part of the game tree if it
# detects that this branch will never be relevant to the overall search.
# If depth is the max depth, returns the score given by a heuristic function
def MaxieMoveAlphaBeta(board, depth, alpha, beta):
    assert(alpha < beta)
    if board.gameOver():
        return (None, ∞) if board.won("Maxie") else (None, -∞)
    else if depth == maxDepth:
        return (None, heuristic(board))
    else:
        bestMove = None
        bestScore = -∞
        for move in board.legalMoves("Maxie"):
            board.makeMove(move)
            _, moveScore = MinnieMoveAlphaBeta(board, depth + 1, alpha, beta)
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
    assert(alpha < beta)
    if board.gameOver():
        return (None, -∞) if board.won("Minnie") else (None, ∞)
    else if depth == maxDepth:
        return heuristic(board)
    else:
        bestMove = None
        bestScore = ∞
        for move in board.legalMoves("Minnie"):
            board.makeMove(move)
            _, moveScore = MaxieMoveAlphaBeta(board, depth + 1, alpha, beta)
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
        self.board = makeBoard()
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
                    if board[row][col] != "W":
                        break
                    else:
                        if col - 1 >= 0 and \
                           board[row + 1][col - 1] == "1":
                            moves += [(row, col, row + 1, col - 1, False)]
                        if col + 1 <= len(board[row]) and \
                           board[row + 1][col + 1] == "1":
                            moves += [(row, col, row + 1, col + 1, False)]
                        if col - 2 >= 0 and \
                           row + 2 <= len(board) and \
                           board[row + 1][col - 1] == "B" and \
                           board[row + 2][col - 2] == "1":
                            moves += [(row, col, row + 2, col - 2, True, row + 1, col - 1)]
                        if col + 2 <= len(board[row]) and \
                           row + 2 <= len(board) and \
                           board[row + 1][col + 1] == "B" and \
                           board[row + 2][col + 2] == "1":
                            moves += [(row, col, row + 2, col + 2, True, row + 1, col + 1)]
        if player == "Maxie":
            for row in range(1, len(board)):
                for col in range(len(board[row])):
                    if board[row][col] != "B":
                        break
                    else:
                        if col - 1 >= 0 and \
                           board[row - 1][col - 1] == "1":
                            moves += [(row, col, row - 1, col - 1, False)]
                        if col + 1 <= len(board[row]) and \
                           board[row - 1][col + 1] == "1":
                            moves += [(row, col, row - 1, col + 1, False)]
                        if col - 2 >= 0 and \
                           row - 2 >= 0 and \
                           board[row - 1][col - 1] == "W" and \
                           board[row - 2][col - 2] == "1":
                            moves += [(row, col, row - 2, col - 2, True, row - 1, col - 1)]
                        if col + 2 <= len(board[row]) and \
                           row - 2 >= 0 and \
                           board[row - 1][col + 1] == "W" and \
                           board[row - 2][col + 2] == "1":
                            moves += [(row, col, row - 2, col + 2, True, row - 1, col + 1)]
        return moves
        
    def makeMove(self, move):
        row = move[0]
        col = move[1]
        newRow = move[2]
        newCol = move[3]
        isJump = move[4]
        board[row][col], board[newRow][newCol] = board[newRow][newCol], board[row][col]
        if isJump:
            jumpedRow = move[5]
            jumpedCol = move[6]
            board[jumpedRow][jumpedCol] = "1"
        
    
    def undoMove(self, move, player):
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
            else:
                jumpedPiece = "W"
            board[jumpedRow][jumpedCol] = jumpedPiece
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    