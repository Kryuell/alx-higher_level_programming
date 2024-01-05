#!/usr/bin/python3
"""
N Queens puzzle solution
"""

import sys


def print_solution(board_size, solutions):
    """Print the solutions in the specified format"""
    for solution in solutions:
        print([[row, col] for row, col in enumerate(solution)])


def is_safe(board, row, col):
    """Check if it's safe to place a queen at a given position"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(board_size, row, board, solutions):
    """Recursively solve N Queens problem using backtracking"""
    if row == board_size:
        solutions.append(board.copy())
    else:
        for col in range(board_size):
            if is_safe(board, row, col):
                board[row] = col
                solve_nqueens(board_size, row + 1, board, solutions)


def nqueens(N):
    """Main function to solve the N Queens problem"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    print_solution(N, solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
