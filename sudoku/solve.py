from board import board


def solve(board):
    endidx = 9*9
    def backtrack(idx):
        if idx == endidx:
            return True
    
        if board[idx] != 0:
            return backtrack(idx + 1)

        for i in range(9):
            if board.validInsertion(i+1, idx):
                board.insert(i+1, idx)
                if backtrack(idx+1):
                    return True
        board.insert(0, idx)
        return False
    backtrack(0)


    
    
