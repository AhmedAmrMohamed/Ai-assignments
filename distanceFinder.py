from board import board
import constants as consts
import utils

def binaryDistance(alpha, beta):
    for itr in utils.matrixIterator():
        alphaval = alpha[itr]
        betaval = beta[itr]
        if alphaval != betaval:
            return 1 
    return 0

def heuristicDistance(alpha, beta):
    distance = 0
    for itr in utils.matrixIterator():
        if alpha[itr] != beta[itr]:
            distance += 1
    return distance

    
