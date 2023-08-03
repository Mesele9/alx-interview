#!/usr/bin/python3
""" 0-nqueens.py """
import sys


def is_safe(board, row, col, N):
    """ a function for checking the presence of queen """
    # check for queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # check for queen in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # check for queen in the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, row, N, solutions):
    """ helper function """
    if row == N:
        solution = [[i, j] for i in range(N)
                    for j in range(N) if board[i][j] == 1]
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, N, solutions)
            board[row][col] = 0


def solve_nqueens(N):
    """ a function for solve the N queen problem """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at leat 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    solve_nqueens(N)

