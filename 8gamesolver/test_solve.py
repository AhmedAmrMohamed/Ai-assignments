from board import board
import utils
from distanceFinder import *
import solve

def noZero():
    return board([1,2,0,4,4,5,6,7,8])


def testite():
    for i in utils.matrixIterator():
        print(i)


def test_binaryDistance():
    a = board([1,2,0,4,4,5,6,7,8])
    b = board([1,2,0,4,4,5,6,7,8])
    df = distanceFinder(a, b)
    di = df.binaryDistance()
    print(di)
    assert(di == 0)
    return a, b, df, di

def test_solve_0():
    a = board([1,2,0,3,4,5,6,7,8])
    b = board([1,2,0,3,4,5,6,7,8])
    s = solve.solver(a, b)
    print(s.res[0])
    moveboard(s.res[1], a)


def test_solve_1():
    a = board([1,0,2,3,4,5,6,7,8])
    b = board([1,2,0,3,4,5,6,7,8])
    s = solve.solver(a, b)
    print(s.res[0])
    moveboard(s.res[1], a)

def test_solve_3():
    a = board([1,0,2,3,4,5,6,7,8])
    b = board([1,4,2,3,7,5,6,0,8])
    print('a', a, 'b', b, sep ='\n')
    s = solve.solver(a, b)
    print("solved in ", len(s.res[1]))
    moveboard(s.res[1], a)

def test_solve_4():
    a = board([1,2,3,4,0,5,6,7,8])
    b = board([1,3,5,4,2,0,6,7,8])
    print('a', a, 'b', b, sep ='\n')
    s = solve.solver(a, b)
    print("solved in ", len(s.res[1]))
    moveboard(s.res[1], a)

def test_solve_5():
    x = [i for i in range(9)]
    a = board(x)
    x.reverse()
    b = board(x)
    print('a', a, 'b', b, sep ='\n')
    s = solve.solver(a, b)
    print("solved in ", len(s.res[1]))
    moveboard(s.res[1], a)

def test_solve_6():
    from random import shuffle
    org = [i for i in range(9)]
    shuffle(org)
    a = board(org[:])
    shuffle(org)
    b = board(org[:])
    print('a', a, 'b', b, sep ='\n')
    s = solve.solver(a, b)
    print("solved in ", len(s.res[1]))
    moveboard(s.res[1], a)




def moveboard(moves, board):
    print('moving:\n', board, sep ="")
    for move in moves:
        board.move(move)
        print(board)

#test_solve_3()
#test_solve_4()
#test_solve_5()
#test_solve_5()
#test_solve_6()

