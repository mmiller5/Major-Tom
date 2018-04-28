# Rudimentary AI for the checkers puzzle
'''
Alpha-Beta Minimax code written by Eric Clinch
https://drive.google.com/drive/folders/1lLCArvni4VB6sL6wTP3qZv-B8_lX2kxX
modified by me
'''
from puzzle2Logic import *

def MaxieMoveAlphaBeta(board, depth, alpha, beta):
    assert(alpha < beta)
    if False:#board.isGameOver():
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
    assert(alpha < beta)
    if False:#board.isGameOver():
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

def getMove(board, depth, alpha=-100, beta=100):
    move = MinnieMoveAlphaBeta(board, depth, alpha, beta)
    print(move)
    return move[0]
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