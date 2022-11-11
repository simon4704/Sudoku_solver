# Sudoku_solver

Solves/bruteforces sudokus using recursive backtracking.

The solver starts in the top-left corner and works its way right, then down, increasing the value for each square by 1 and checking if the new value is valid. If yes, move on tho the next square, if no, go one step back and increase that number by 1. If a value is increased beyond 9, reset it to 1, go one step further back and increase this value by 1. Repeat until all values are valid and the sudoku is solved.
