# generates boards for puzzle 3
import random
import copy

def puzzle3Generate():
    board = []
    numbers = [1, 1, 2, 2, 3, 3]
    result = solve(board, numbers)
    result = upsAndDowns(result)
    return result

def solve(board, numbers):
    if len(board) == 6:
        return board
    else:
        random.shuffle(numbers)
        for i in range(len(numbers)):
            board.append(numbers.pop(i))
            if isLegal(board):
                move = solve(board, numbers)
                if move != None:
                    return move
            numbers.insert(i, board.pop())
    return None
    
def isLegal(board):
    for i in range(len(board) - 1):
        if board[i] == board[i + 1]:
            return False
    return True
    
def upsAndDowns(board):
    result = []
    d = dict()
    positions = ["Down", "Up"]
    for i in range(1, 4):
        option = positions
        random.shuffle(option)
        d[i] = [False, tuple(option)]
    for item in board:
        if d[item][0]:
            result.append([d[item][1][1], item])
        else:
            result.append([d[item][1][0], item])
            d[item][0] = True
    return result