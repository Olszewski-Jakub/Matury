def game_of_life(tests):
    for _ in range(tests):
        board = read_board()
        for _ in range(100):
            next_board = copy_board(board)
            for i in range(5):
                for j in range(5):
                    check_cell(board, next_board, i, j)
            board = next_board
        if is_alive(board):
            print("yes")
        else:
            print("no")

def check_cell(board, next_board, i, j):
    count = count_neighbours(board, i, j)
    if board[i][j] == 1:
        if count < 2 or count > 3:
            next_board[i][j] = 0
    else:
        if count == 3:
            next_board[i][j] = 1

def count_neighbours(board, i, j):
    count = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x == i and y == j:
                continue
            x = x % 5
            y = y % 5
            if board[x][y] == 1:
                count += 1
    return count

def is_alive(board):
    for i in range(5):
        for j in range(5):
            if board[i][j] == 1:
                return True
    return False

def read_board():
    board = []
    for _ in range(5):
        board.append([int(c) for c in input()])
    return board

def copy_board(board):
    return [row[:] for row in board]

tests = int(input())
game_of_life(tests)