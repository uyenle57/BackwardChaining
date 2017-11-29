# -*- coding: utf-8 -*-#


class InferenceEngine():
    """ This represents the application's Inference Engine """

    # Initialise frontier and explored set
    frontier = [] # empty stack
    explored = {} # empty set

    def __init__(self):
        pass

    def depth_first_search(self, initial_state, goal):
        """ Performs Depth-First search strategy, returns success or failure """

        self.frontier = [initial_state]

        # Make sure frontier is not empty, otherwise fail the program
        while not self.frontier:
            state = self.frontier.pop() # Remove last element of the Stack
            explored.append(self.state)

            # Goal test: returns success if goal is found.
            if(state == goal):
                print("Success")
                return

            for neighbor in state.neighbors():
                if not neighbor in:
                    frontier.append(state)
        return

    def match_goal(self, goal):
        """ Match a goal with a consequent, using Backward Chaining operating with Depth-First Search"""
        pass

    # Match a subgoal with antecedents from a rule
    def match_subgoal(self, subgoal):
        pass

    # Select function
    def select(self):
        pass

    # Act function
    def act(self):
        pass
