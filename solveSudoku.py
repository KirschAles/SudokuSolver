import time
import solver
from SudokuBoard import SudokuBoard
import sys


# input is in format python solveSudoku.py <nameOfFile>
# reads unsolved sudoku in the file and then solves it
# empty space is 0 by default and the different positions in a row  must be separated by ' '
# ouputs solve sudoku and the time it took the algorithm to solve it
def main():
    separator = " "
    emptySpace = 0
    # create a simple board, size doesn't matter, .read command will change it automatically
    problem = SudokuBoard(1)
    try:
        problem.read(sys.argv[1], sep=separator)
    except Exception as e:
        print("You must enter the name of file.")
        return
    # write unsolved problem
    problem.print(sep=" ")

    start = time.time()
    solution = solver.solveSudoku(problem)
    end = time.time()

    if solution is None:
        print("No solution was found.")
    else:
        print("Solved:")
        solution.print()
    print("The sudoku was solved in: ", end="")
    print(str(end - start) + " seconds")


if __name__ == '__main__':
    main()


