import random
import copy
import math

class SudokuBoard:
    def __init__(self, dimension=3, empty=0):
        self.dimension = dimension
        self.board = [[0 for i in range(dimension**2)] for j in range(dimension**2)]
        self.validNumbers = [n for n in range(1, dimension**2 + 1)]
        self.empty = empty

    def isOnBoard(self, x, y):
        if self.dimension**2 > x and x >= 0 and self.dimension**2 > y and y >= 0:
            return True
        return False
    def numbers(self):
        return self.validNumbers
    def numbersRandomSort(self):
        numbers = self.numbers().copy()
        randomNumbers = []
        while numbers != []:
            number = random.choice(numbers)
            randomNumbers.append(number)
            numbers.remove(number)
        return randomNumbers

    def at(self, x, y):
        if self.isOnBoard(x, y):
            return self.board[y][x]
        raise ValueError("Position is out of bounds.")
    def isEmpty(self, x, y):
        try:
            return self.at(x, y) == self.empty
        except ValueError as e:
            return False
    def next(self, x, y):
        newX = (x+1) % self.dimension**2
        newY = y
        if newX < x:
            newY = y+1
            if newY >= self.dimension**2:
                raise ValueError("This position was the last.")
        return (newX, newY)


    def assign(self, position, value):
        if self.isOnBoard(position[0], position[1]):
            self.board[position[1]][position[0]] = value
            return
        raise ValueError("Position is out of bounds.")

    def print(self, sep=''):
        for y in range(self.dimension**2):
            for x in range(self.dimension**2):
                print(self.at(x, y), end=sep)
            print()

    def copy(self):
        newBoard = SudokuBoard(self.dimension)
        newBoard.board = copy.deepcopy(self.board.copy())
        return newBoard
    def write(self, fileName, sep=" "):
        file = open(fileName, 'w')
        for y in range(self.dimension**2):
            for x in range(self.dimension**2):
                file.write(str(self.at(x,y)) + str(sep))
            file.write("\n")
        file.close()


    def read(self, fileName, sep=" "):
        file = open(fileName, "r")
        self.board = []
        for i in file.readlines():
            line = i.strip("\n").strip(sep).split(sep)
            for j in range(len(line)):
                line[j] = int(line[j])
            self.board.append(line)
        self.dimension = math.floor(math.sqrt(len(self.board)))
        self.validNumbers = [n for n in range(1, self.dimension**2 + 1)]
        self.empty = 0
        file.close()
