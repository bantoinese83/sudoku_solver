import cProfile
import sys
from halo import Halo


def is_valid(board, row, col, num):
    """
    Checks if placing `num` at `(row, col)` are valid.

    Args:
        board (list of int): The Sudoku board.
        row (int): The row index.
        col (int): The column index.
        num (int): The number to place.

    Returns:
        bool: True if placing `num` is valid, False otherwise.
    """
    # Check the row and column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    # Check the 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    """
    Solves the Sudoku puzzle using backtracking.

    Args:
        board (list of list of int): The Sudoku board.

    Returns:
        bool: True if the Sudoku is solved, False otherwise.
    """
    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def find_empty(board):
    """
    Finds the first empty cell on the board.

    Args:
        board (list of list of int): The Sudoku board.

    Returns:
        tuple: The row and column index of the first empty cell, or None if no empty cell is found.
    """
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def print_board(board):
    """
    Prints the Sudoku board with visual separators.

    Args:
        board (list of list of int): The Sudoku board.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)

        line = ""
        for j in range(9):
            if j % 3 == 0 and j != 0:
                line += " | "
            line += str(board[i][j]) if board[i][j] != 0 else "."
            line += " "
        print(line)
    sys.stdout.flush()


def pre_filter(board):
    """
    Pre-filters the board to identify cells with only one possible value.

    Args:
        board (list of list of int): The Sudoku board.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                possible_nums = set(range(1, 10))
                for i in range(9):
                    possible_nums.discard(board[row][i])
                    possible_nums.discard(board[i][col])

                start_row, start_col = 3 * (row // 3), 3 * (col // 3)
                for i in range(start_row, start_row + 3):
                    for j in range(start_col, start_col + 3):
                        possible_nums.discard(board[i][j])

                if len(possible_nums) == 1:
                    board[row][col] = possible_nums.pop()


def generate_sudoku(difficulty):
    """
    Generates a Sudoku puzzle of the specified difficulty.

    Args:
        difficulty (str): The difficulty level ('easy', 'medium', 'hard', 'expert').

    Returns:
        list of list of int: The generated Sudoku puzzle.
    """
    if difficulty == 'easy':
        # Generate an easy puzzle
        return [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
    elif difficulty == 'medium':
        # Generate a medium puzzle
        return [
            [0, 0, 0, 2, 6, 0, 7, 0, 1],
            [6, 8, 0, 0, 7, 0, 0, 9, 0],
            [1, 9, 0, 0, 0, 4, 5, 0, 0],
            [8, 2, 0, 1, 0, 0, 0, 4, 0],
            [0, 0, 4, 6, 0, 2, 9, 0, 0],
            [0, 5, 0, 0, 0, 3, 0, 2, 8],
            [0, 0, 9, 3, 0, 0, 0, 7, 4],
            [0, 4, 0, 0, 5, 0, 0, 3, 6],
            [7, 0, 3, 0, 1, 8, 0, 0, 0]
        ]
    elif difficulty == 'hard':
        # Generate a hard puzzle
        return [
            [0, 0, 0, 6, 0, 0, 4, 0, 0],
            [7, 0, 0, 0, 0, 3, 6, 0, 0],
            [0, 0, 0, 0, 9, 1, 0, 8, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 5, 0, 1, 8, 0, 0, 0, 3],
            [0, 0, 0, 3, 0, 6, 0, 4, 5],
            [0, 4, 0, 2, 0, 0, 0, 6, 0],
            [9, 0, 3, 0, 0, 0, 0, 0, 0],
            [0, 2, 0, 0, 0, 0, 1, 0, 0]
        ]
    elif difficulty == 'expert':
        # Generate an expert puzzle
        return [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 0, 8, 5],
            [0, 0, 1, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 5, 0, 7, 0, 0, 0],
            [0, 0, 4, 0, 0, 0, 1, 0, 0],
            [0, 9, 0, 0, 0, 0, 0, 0, 0],
            [5, 0, 0, 0, 0, 0, 0, 7, 3],
            [0, 0, 2, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 4, 0, 0, 0, 9]
        ]
    else:
        raise ValueError("Invalid difficulty level. Choose from 'easy', 'medium', 'hard', 'expert'.")


def main():
    """
    Main function to solve and print the Sudoku puzzle.
    """
    difficulty_level = input("Enter difficulty level ('easy', 'medium', 'hard', 'expert'): ")
    sudoku_board = generate_sudoku(difficulty_level)

    pre_filter(sudoku_board)

    spinner = Halo(text='Solving Sudoku...', spinner='dots')
    spinner.start()

    if solve_sudoku(sudoku_board):
        spinner.succeed("Sudoku solved!")
        print("Solved Sudoku:")
        print_board(sudoku_board)
    else:
        spinner.fail("No solution exists.")
        print("No solution exists.")


if __name__ == "__main__":
    cProfile.run('main()')