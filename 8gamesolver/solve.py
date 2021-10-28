from board import board
from heap import heap
import distanceFinder
import directions 
import sys

class solver():
    def __init__(self, initial, target):
        self.initial = initial
        self.target = target
        self.visited = {}
        self.heap = heap(max = False, key = lambda a, b: a[0] < b[0])
        self.res = self.solve(initial)

    def solve(self, current, lastDire = None):
        s_visited = self.visited
        s_heap = self.heap
        
        self.heapInsert(current, [])
        while not s_heap.empty():
            # stop when a result is found or the queue is empty
            hdist, currentState, steps = s_heap.pop()
            if self.isTargetFound(currentState):
                return True, steps
                
            s_visited[currentState] = True
            for nextstate, nextstep in self.adjacentStatesOf(currentState):
                tmp = steps[:]
                tmp.append(nextstep)
                self.heapInsert(nextstate, tmp)
        return False, None

    def adjacentStatesOf(self, state):
        ret = []
        for dire in directions.directions:
            nodeClone = state.clone()
            if nodeClone.move(dire):
                if self.isVisited(nodeClone):
                    continue
                else:
                    ret.append((nodeClone, dire))
        return ret

    def isTargetFound(self, A):
        return distanceFinder.binaryDistance(A, self.target) == 0

    def isVisited(self, board):
        for state in self.visited.keys():
            if distanceFinder.binaryDistance(state, board) == 0:
                return True
        return False

    def heapInsert(self, node, steps):
        hdist = distanceFinder.heuristicDistance(node, self.target)
        score = len(steps) + hdist
        self.heap.insert((hdist, node, steps))
        