# -*- coding: utf-8 -*-#

import sys

class DepthFirstSearch(object):
    """ Performs Depth-First search strategy, returns success or failure """

    frontier = []
    explored = []

    def __init__(self):
        pass

    def execute(self, initial_state, goal):

        self.frontier = [initial_state]

        # Make sure frontier is not empty, otherwise fail the program
        if not self.frontier:
            print("\nFAILURE: Frontier is empty.\n")
            sys.exit(1)

        state = self.frontier.pop()
        self.explored.append(state)

        # Goal test: returns success if goal is found
        if state == goal:
            print("Goal found:", goal)
            sys.exit(0)

        for i in state.neighbors():
            if not self.in_list(self.frontier, i) and self.in_list(self.explored, i):
                self.frontier.append(i)


    def in_list(self, a, b):
        pass
