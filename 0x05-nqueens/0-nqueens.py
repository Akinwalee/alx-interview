#!/usr/bin/python3


import sys


def main():
    """
    Entry point.
    Validate the input number and hand it to the helper functions.
    Print the possible solutions
    """
    if len(sys.argv) != 2:
        print_usage_and_exit()
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)

    for solution in solutions:
        print(solution)

def solve_nqueens(N):
    """
    Backtracking function to find all possible solutions.
    """
    def backtrack(row, board, solutions):
        """
        Recursive backtracking function to solve the N queens.
        """
        if row == N:
            solutions.append([[i, board[i]] for i in range(N)])
            return
        
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                backtrack(row + 1, board, solutions)
                board[row] = -1  # Reset for backtracking

    solutions = []
    board = [-1] * N  # board[row] = column where the queen is placed
    backtrack(0, board, solutions)
    return solutions

# Helpers

def print_usage_and_exit():
    """Print usage message and exit."""
    print("Usage: nqueens N")
    sys.exit(1)

def is_safe(board, row, col, N):
    """
    Check if placing a queen at a coordinate is safe
    """
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

if __name__ == "__main__":
    main()
