#!/usr/bin/python3import sys
import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check the lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, solutions):
    """
    Recursive function to solve the N Queens problem using backtracking
    """
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1

            # Recur to place the rest of the queens
            solve_n_queens(board, col + 1, solutions)

            # Backtrack and remove the queen from board[i][col]
            board[i][col] = 0

    return False


def print_solutions(solutions):
    """
    Print the solutions to the N Queens problem
    """
    for solution in solutions:
        print(solution)


def nqueens(n):
    """
    Solve the N Queens problem for a given N
    """
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, solutions)
    print_solutions(solutions[::-1])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
