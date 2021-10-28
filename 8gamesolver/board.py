from boardAssertions import checkInputNumbers
from directions import directions
import constants as consts
import utils

class board:
    def __init__(self, numbers):
        checkInputNumbers(numbers) 
        self.matrix = self.buildMatrix(numbers)
        self.zeroRow, self.zeroCol = self.findOriginalZeroPos(numbers)

    def __getitem__(self, cor):
        return self.matrix[cor[0]][cor[1]]

    def clone(self):
        fm = utils.flattenMatrix(self.matrix)
        return board(fm)
    
    def __repr__(self):
        stringbuilder = []
        for row in self.matrix:
            for col in row:
                stringbuilder.append(str(col))
                stringbuilder.append(str(' '))
            stringbuilder.append('\n')
        return "".join(stringbuilder)

    def __str__(self):
        return self.__repr__()
    
    def buildMatrix(self, numbers):
        matrix = [[0 for i in range(consts.BOARD_DIMENSION)]\
                for j in range(consts.BOARD_DIMENSION)]
        
        for idx in range(consts.BOARD_NUM_COUNT):
            row, col = utils.rowAndCol(idx) 
            matrix[row][col] = numbers[idx]

        return matrix
    
    def findOriginalZeroPos(self, numbers):
        idx = numbers.index(0)
        return utils.rowAndCol(idx)

    def isValidZeroPos(self, row, col):
        return row >= 0 and row < consts.BOARD_DIMENSION\
                and col >= 0 and col < consts.BOARD_DIMENSION 
        
    def move(self, direction):
        newrow =  self.zeroRow + directions[direction][0]
        newcol =  self.zeroCol + directions[direction][1]
        if self.isValidZeroPos(newrow, newcol) == False:
            return False
        self.swap(newrow, newcol, self.zeroRow, self.zeroCol)
        self.zeroRow = newrow
        self.zeroCol = newcol
        return True
    
    def swap(self, Arow, Acol, Brow, Bcol):
        tmp = self.matrix[Arow][Acol]
        self.matrix[Arow][Acol] = self.matrix[Brow][Bcol]
        self.matrix[Brow][Bcol] = tmp

    def flaten(self):
        return utils.flattenMatrix(self.matrix)

    
