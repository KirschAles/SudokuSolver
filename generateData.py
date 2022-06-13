import time
from sudokuGenerator import generateSudoku
from solver import solveSudoku
import csv


def countEmptiness(sudoku):
    count = 0
    for i in range(sudoku.dimension**2):
        for j in range(sudoku.dimension**2):
            if sudoku.isEmpty(i, j):
                count += 1
    return count

# generate and than solve one dataPoint
def oneOff(dimension, empty, depth):
    sudoku = generateSudoku(dimension, empty, depth)
    emptyCount = countEmptiness(sudoku)
    start = time.time()
    solveSudoku(sudoku)
    end = time.time()
    duration = end-start
    return(emptyCount, duration)


from sys import argv
from sys import exit


if __name__ == "__main__":
    dimension = 3
    countPerDepth = 10
    if len(argv) != 2:
        print("Command format: command <fileName>.csv")
        exit()
    with open(argv[1], 'w', newline='') as csvFile:
        maxDepth = dimension**4
        writer = csv.writer(csvFile)
        writer.writerow(['depth', 'duration'])
        # 14 is the lowest count of nonEmpty spaces that can lead to a unique solution
        # when dimension is 3
        for depth in range(maxDepth-1, 13, -4):
            print("Now on depth: " + str(depth))
            for take in range(countPerDepth):
                emptySpaces, duration = oneOff(dimension, 0, depth)
                writer.writerow([emptySpaces, duration])