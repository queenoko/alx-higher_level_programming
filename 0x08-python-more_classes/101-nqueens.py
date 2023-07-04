#!/usr/bin/python3
# 101-nqueens.py

"""solve N-queen puzzle

Determine all possible solution to pacing N
N non-attacking queen on an NxN chessboard

E.g:
    $ ./101-nqueens.py N

    N must be integer that is greater tan or equals to 4

    Attrib:
    board (list): List of lists representing chessboard
    solutions (list): list of lists containing solutions.

    Solutions are represented inthe format [[r, c], [r, c], [r, c], [r, c]]
    where `r` and `c` represent row and column, where queen is on chessboard
    """
import sys


def init_board(n):
    """initialize `n`x`n` sized chessboard with 0's"""
    board = []
    [board.append([]) for z in range(n)]
    [row.append(' ') for z in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Returns deep copy of chessboard"""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Returns list of lists representation of solved chessboard"""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """X out spot on a chessboard
    All spots where non-attacking queens can no longer
    be played are X-ed out

    Arg:
    board (list): Current working chessboard
    row (int): Row where queen was last played
    col (int): Column where queen was last played
    """
    # X out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # X out all backward spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # X out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # X out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # X out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solving an N-queens puzzle

    Arg:
    board (list): current working chessboard
    row (int): current working row
    queen (int): current number of placed queens
    solutions (list): list of lists of solutions
    Returns:
    solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, solutions)
    return (solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usuage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
