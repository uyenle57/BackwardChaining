# -*- coding: utf-8 -*-#

from BackwardChaining.WorkingMemory import WorkingMemory
from BackwardChaining.KnowledgeBase import KnowledgeBase
# from BackwardChaining.DepthFirstSearch import DepthFirstSearch
import sys


class InferenceEngine(object):
    """ Represents the application's Inference Engine: Match -> Select -> Act using Backward Chaining """

    def __init__(self):
        pass

    @staticmethod
    def depth_first_search(graph, start, goal):
        """ Performs Depth First Search, returns success for failure """

        # Adapted from http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

        #  Initialise frontier with the (consequent, antecedent) tuple structure
        frontier = [(start, [start])]

        print("Frontier: ", frontier)

        # Run if frontier is not empty
        while frontier:
            (consequent, antecedent) = frontier.pop()

            for i in graph[consequent] - set(antecedent):

                if i == goal:
                    yield antecedent + [i]  # returns a generator
                    print(antecedent + [i])
                    print("SUCCESS - Goal found:", goal)
                else:
                    frontier.append((i, antecedent + [i]))

    def match_goal(self, goal):
        """ Match a goal with a consequent, using Depth-First Search """

        # workingMemory = WorkingMemory()
        # knowledgeBase = KnowledgeBase()
        #
        # rules = knowledgeBase.get_rules()
        #
        #     # for each rule whose consequent matches this hypothesis
        # for i in range(0, len(rules)):
        #     if rules[i].get_consequent() == goal:
        #         print("dsfsfsf", rules[i].get_antecendents)
        pass

    def match_subgoal(self, subgoal):
        """ Match a sub-goal with antecedents from a rule, using Depth-First Search """
        pass

    def select(self):
        pass

    def act(self):
        pass
