# Sudoku Solver 🧩

This project is a Sudoku solver implemented in Python. It includes functions to generate Sudoku puzzles of varying difficulty, solve them using backtracking, and provide visual feedback during the solving process using the `halo` library.

## Features ✨

- Generate Sudoku puzzles of different difficulty levels (`easy`, `medium`, `hard`, `expert`).
- Solve Sudoku puzzles using a backtracking algorithm.
- Pre-filter the board to identify cells with only one possible value.
- Provide visual feedback during the solving process with a spinner.

## Requirements 📦

- Python 3.x
- `halo` library

## Installation 🛠️

1. Clone the repository: 
    ```sh
    git clone https://github.com/bantoinese83/sudoku_solver.git
    cd sudoku_solver
    ```

2. Install the required dependencies:
    ```sh
    pip install halo
    ```

## Usage 🚀

Run the main script to generate and solve a Sudoku puzzle:

```sh
python sudoku_solver.py
```

The script will generate a Sudoku puzzle of random difficulty, display the initial board, solve it, and display the solved board. 
