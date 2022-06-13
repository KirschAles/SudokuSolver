from satisfiesConstraints import satisfiesConstraints


def findEmptyPlaces(sudoku, x, y):
    emptyPlaces = []
    while True:
        if sudoku.at(x, y) == sudoku.empty:
            emptyPlaces.append((x, y))
        try:
            (x, y) = sudoku.next(x, y)
        except ValueError as e:
            return emptyPlaces


def solveSudoku(sudoku, x=0, y=0):
    emptyPlaces = findEmptyPlaces(sudoku, x, y)
    return CSP(sudoku, sudoku.numbers(), satisfiesConstraints, emptyPlaces)

# variables is the current state of the board
# domain are the numbers that can possibly be put into empty spaces
# satisfiesConstraints is a function that checks if the new addition satisfies all constraints
# toBeFilled is a list of places, where a new value should be put,
# is not necceserally needed but speeds up the execution time, by not havind to
# find the next empty space in every iteration\
# return either the solved problem or None if no solution exists
def CSP(variables, domain, satisfiesConstraints, toBeFilled):
    if len(toBeFilled) == 0:
        return variables
    solution = None
    for value in domain:
        if satisfiesConstraints(toBeFilled[0], value, variables):
            variables.assign(toBeFilled[0], value)
            usedPos = toBeFilled.pop(0)
            solution = CSP(variables, domain, satisfiesConstraints, toBeFilled)
            if not solution is None:
                return solution
            variables.assign(usedPos, variables.empty)
            toBeFilled.insert(0, usedPos)
    return solution