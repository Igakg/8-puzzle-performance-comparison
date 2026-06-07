# ==============================================================================
# Original File: iddfs.py
# Copyright (C) abpaudel (https://github.com/abpaudel/8-puzzle)
#
# This file is part of "8-puzzle" and is licensed under the 
# GNU General Public License v3.0 (GPLv3).
# See <https://www.gnu.org/licenses/gpl-3.0.en.html> for details.
# ==============================================================================
import itertools

from solver import Solver


class IDS(Solver):
    def __init__(self, initial_state):
        super(IDS, self).__init__(initial_state)
        self.frontier = []

    def dls(self, limit):
        self.frontier.append(self.initial_state)
        while self.frontier:
            board = self.frontier.pop()
            self.explored_nodes.add(tuple(board.state))
            if board.goal_test():
                self.set_solution(board)
                return self.solution
            if board.depth < limit:
                for neighbor in board.neighbors()[::-1]:
                    if tuple(neighbor.state) not in self.explored_nodes:
                        self.frontier.append(neighbor)
                        self.explored_nodes.add(tuple(neighbor.state))
                        self.max_depth = max(self.max_depth, neighbor.depth)
        return None

    def solve(self):
        for i in itertools.count():
            self.frontier = []
            self.explored_nodes = set()
            self.max_depth = 0
            self.frontier.append(self.initial_state)
            sol = self.dls(i)
            if sol is not None:
                break
        return