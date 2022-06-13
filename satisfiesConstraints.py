def satisfiesRowConstraint(row, value, sudoku):
    for column in range(sudoku.dimension**2):
        if sudoku.at(column, row) == value:
            return False
    return True


def satisfiesColumnConstraint(column, value, sudoku):
    for row in range(sudoku.dimension**2):
        if sudoku.at(column, row) == value:
            return False
    return True


def satisfiesSmallBoardConstraint(x, y, value, sudoku):
    startingX = x // sudoku.dimension * sudoku.dimension
    startingY = y // sudoku.dimension * sudoku.dimension
    for y in range(startingY, startingY+sudoku.dimension):
        for x in range(startingX, startingX+sudoku.dimension):
            if sudoku.at(x, y) == value:
                return False
    return True

def satisfiesConstraints(position, value, sudoku):
    x = position[0]
    y = position[1]
    if satisfiesRowConstraint(y, value, sudoku) \
     and satisfiesColumnConstraint(x, value, sudoku) \
     and satisfiesSmallBoardConstraint(x, y, value, sudoku):
        return True
    return False