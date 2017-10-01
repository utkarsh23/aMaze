from random import choice

class Cell:
    def __init__(self, n):
        self.N = True
        self.S = True
        self.W = True
        self.E = True
        self.neighbourN = None
        self.neighbourS = None
        self.neighbourW = None
        self.neighbourE = None
        self.occupied = False
        self.number = n

class Grid:
    def __init__(self, size=10):
        self.side = size
        self.stack = []
        self.cells = [Cell(i) for i in range(self.side ** 2)]
        for j in self.cells:
            if j.number not in range(self.side ** 2)[:self.side]:
                j.neighbourN = self.cells[j.number - self.side]
            if j.number not in range(self.side ** 2)[(self.side ** 2 - self.side):]:
                j.neighbourS = self.cells[j.number + self.side]
            if (j.number % self.side) != 0:
                j.neighbourW = self.cells[j.number - 1]
            if (j.number % self.side) != (self.side - 1):
                j.neighbourE = self.cells[j.number + 1]
        self.generate()

    def __str__(self):
        toReturn = ("  " + ("_" * ((self.side * 2) - 3))) + "\n"
        for a in self.cells:
            if a.number % self.side == 0:
                toReturn += "|"
            if a.S:
                toReturn += "_"
            else:
                toReturn += " "
            if a.E:
                toReturn += "|"
            else:
                toReturn += " "
            if (a.number % self.side) == (self.side - 1):
                toReturn += "\n"
        return toReturn

    def generate(self):
        currentCell = choice(self.cells)
        visitedCells = 1
        while visitedCells != self.side ** 2:
            choices = []
            if currentCell.neighbourN and not currentCell.neighbourN.occupied:
                choices.append(currentCell.neighbourN)
            if currentCell.neighbourS and not currentCell.neighbourS.occupied:
                choices.append(currentCell.neighbourS)
            if currentCell.neighbourW and not currentCell.neighbourW.occupied:
                choices.append(currentCell.neighbourW)
            if currentCell.neighbourE and not currentCell.neighbourE.occupied:
                choices.append(currentCell.neighbourE)
            if choices:
                nextCell = choice(choices)
                nextCell.occupied = True
                visitedCells += 1
                self.stack.append(nextCell)
                self.removeWall(currentCell, nextCell)
            else:
                removeCell = self.stack.pop(-1)
                nextCell = self.stack[-1]
            currentCell = nextCell

    def removeWall(self, primary, secondary):
        if primary.neighbourN == secondary:
            primary.N = False
            secondary.S = False
        if primary.neighbourS == secondary:
            primary.S = False
            secondary.N = False
        if primary.neighbourW == secondary:
            primary.W = False
            secondary.E = False
        if primary.neighbourE == secondary:
            primary.E = False
            secondary.W = False