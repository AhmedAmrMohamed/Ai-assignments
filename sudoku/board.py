class board:
    def __init__(self, initialInput):
        self.board = self.buildBoard(initialInput)

    def __repr__(self):
        strbuilder = []
        for row in self.board:
            rowstr = map(str, row)
            strbuilder.append( " ".join(rowstr))
        return '\n'.join(strbuilder)

    def buildBoard(self, initialInput):
        board = []
        itr = 0
        for row in range(9):
            board.append([])
            for col in range(9):
                board[row].append(initialInput[itr])
                itr+=1
        return board

    def sqaureOf(self, row, col):
        return 3*(row//3), 3*(col//3)
   
    def validCellCorr(self, row, col):
        val = lambda x : x > -1 and x < 9
        return val(row) and \
                val(col) and \
                self.board[row][col] == 0
    
    def validInsertion(self, insertion, idx):
        board = self.board
        row, col = self.to2d(idx)
        cond = lambda a, b : board[a][b] == insertion

        for ele in range(9):
            if cond(ele, col):
                return False

        for ele in range(9):
            if cond(row, ele):
                return False
        
        s_row, s_col = self.sqaureOf(row, col)
        for rowitr in range(s_row, s_row+3):
            for colitr in range(s_col, s_col+3):
                print(rowitr, colitr)
                if cond(rowitr, colitr):
                    return False

        return True

    def insert(self, insertion, idx):
        row, col = self.to2d(idx)
        self.board[row][col] = insertion
    
    def to2d(self, idx):
        return idx//9, idx%9

    def __getitem__(self, idx):
        cor = self.to2d(idx)
        return self.board[cor[0]][cor[1]]

