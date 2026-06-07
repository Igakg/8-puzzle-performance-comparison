import heapq
from solver import Solver

class AStar0(Solver):
    def __init__(self, initial_state):
        super(AStar0, self).__init__(initial_state)
        self.frontier = []

    @staticmethod
    def h(board):
        return 0

    def solve(self):
        self.initial_state.cost = self.initial_state.depth + self.h(self.initial_state)
        heapq.heappush(self.frontier, self.initial_state)
        while self.frontier:
            board = heapq.heappop(self.frontier)
            self.explored_nodes.add(tuple(board.state))
            if board.goal_test():
                self.set_solution(board)
                break
            for neighbor in board.neighbors():
                if tuple(neighbor.state) not in self.explored_nodes:
                    neighbor.cost = neighbor.depth + self.h(neighbor)
                    heapq.heappush(self.frontier, neighbor)
                    self.explored_nodes.add(tuple(neighbor.state))
                    self.max_depth = max(self.max_depth, neighbor.depth)
        return