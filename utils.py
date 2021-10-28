import constants as consts

def rowAndCol(idx):
        return idx // consts.BOARD_DIMENSION, idx % consts.BOARD_DIMENSION 

def flattenMatrix(matrix):
    ret = []
    for row in matrix:
        ret.extend(row)
    return ret

class matrixIterator():
    def __iter__(self):
        self.idx = -1
        return self

    def __next__(self):
        if self.idx < consts.BOARD_NUM_COUNT - 1:
            self.idx+=1 
            return rowAndCol(self.idx)
        raise StopIteration
