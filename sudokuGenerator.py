from SudokuBoard import SudokuBoard
from satisfiesConstraints import satisfiesConstraints
import random


def CSPgenerator(domain, satisfiesConstraints, x=0, y=0):
    try:
        (nextX, nextY) = domain.next(x, y)
    except ValueError as e:
        return domain

    solution = None
    for value in domain.numbersRandomSort():
        if satisfiesConstraints((x,y), value, domain):
            domain.assign((x, y), value)
            usedPos = (x, y)
            solution = CSPgenerator(domain, satisfiesConstraints, nextX, nextY)
            if not solution is None:
                return solution
            domain.assign(usedPos, domain.empty)

    return solution


# counts the number of possible solution
# PARAMERS: sudoku is the SudokuBoard on which are the solutions found
#           x, y are the coordinates on the sudoku board
def countSolutions(sudoku, x=0, y=0):
    solution = 0
    while not sudoku.isEmpty(x, y):
        (x, y) = sudoku.next(x, y)
    try:
        (newX, newY) = sudoku.next(x, y)
    except ValueError as e:
        return 1
    for n in sudoku.numbers():
        if satisfiesConstraints((x, y), n, sudoku):
            sudoku.assign((x, y), n)
            solution += countSolutions(sudoku, newX, newY)
            sudoku.assign((x, y), sudoku.empty)
    return solution


def generateSudokuBoard(dimension=3, empty=0):
    board = SudokuBoard(dimension, empty)
    return CSPgenerator(board, satisfiesConstraints)

def createTiles(dimension):
    tiles = []
    for x in range(dimension**2):
        for y in range(dimension**2):
            tiles.append((x, y))
    return tiles


def generateEmptines(board, empty=0, depth=14):
    allTiles = createTiles(board.dimension)
    i = len(allTiles)
    while len(allTiles) != 0 and i > depth:
        tile = random.choice(allTiles)
        allTiles.remove(tile)
        value = board.at(tile[0], tile[1])
        board.assign((tile[0], tile[1]), empty)
        while countSolutions(board) != 1 and len(allTiles) != 0:
            board.assign((tile[0], tile[1]), value)
            tile = random.choice(allTiles)
            allTiles.remove(tile)
            value = board.at(tile[0], tile[1])
            board.assign((tile[0], tile[1]), empty)
        i -= 1
    return board
def generateSudoku(dimension=3, empty=0, depth=14):
    board = generateSudokuBoard(dimension, empty)
    generateEmptines(board, empty, depth)
    return board




def writeProblem(problem, filename):
    problem.write(filename)

def generateProblem(solutionFile, testFile, depth=25, dimension=3, sep=" ", empty=0):
    problem = generateSudokuBoard(dimension, empty)
    writeProblem(problem, solutionFile)
    generateEmptines(problem, empty, depth)
    writeProblem(problem, testFile)


from sys import argv


def main():
    if len(argv) < 3:
        print("Correct format: sudokuGenerator.py <unfilledSudokuPath> <solvedSudokuPath> [optional <wanted number of filled spots>] [optional<dimension>]")
        return
    fileTest = argv[1]
    fileSolution = argv[2]
    dimension = 3
    bestUnfilled = 25
    if (len(argv) > 3):
        try:
            bestUnfilled = int(argv[3])
        except ValueError as e:
            print("Number of unfilled spots must be an integer.")
    if (len(argv) > 4):
        try:
            dimension = int(argv[4])
        except ValueError as e:
            print("Dimension must be an integer.")
    generateProblem(fileSolution, fileTest, depth=bestUnfilled, dimension=dimension, sep=" ")


if __name__ == "__main__":
    main()