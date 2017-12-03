# -*- coding: utf-8 -*-#


class InferenceEngine(object):
    """ Represents the application's Inference Engine: Match -> Select -> Act using Backward Chaining """

    def __init__(self):
        pass

    def depth_first_search(self, graph, start, goal):
        """ Performs Depth First Search, returns success for failure """

        # Adapted from http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

        #  Initialise frontier with the (consequent, antecedent) tuple structure
        frontier = [(start, [start])]

        print("Frontier: ", frontier)

        # Run if frontier is not empty
        while frontier:
            (consequent, antecedent) = frontier.pop()

            # Only consider the consequent (ignore the antecedents)
            for i in graph[consequent] - set(antecedent):

                if i == goal:
                    yield antecedent + [i]  # returns a generator
                    print(antecedent + [i])
                    print("SUCCESS - Goal found:", goal)
                else:
                    frontier.append((i, antecedent + [i]))

    def match_goal(self, graph, working_memory, goal):
        """ Match a goal with a consequent, using Depth-First Search """

        consequences = graph.keys()

        # for c in consequences:
        #     antecedents = graph[c]
        #     print(c, ":", antecedents)

        # Backward Chaining Algorithm - currently not recursive
        for hypothesis in working_memory:
            for consequent in consequences:
                if consequent == hypothesis:

                    antecedents = graph[consequent]

                    # match each antecedents with the facts from working memory using DFS

                    # if all antecedents matched, then success
                    if antecedents == hypothesis:
                        self.depth_first_search(antecedents, hypothesis)
                    else:
                        # if not matched, add as new subgoal
                        self.match_subgoal(antecedents)

                    pass

    def match_subgoal(self, subgoal):
        """ Match a sub-goal with antecedents from a rule, using Depth-First Search """
        pass

    def select(self):
        pass

    def act(self):
        pass
