# -*- coding: utf-8 -*-#

from BackwardChaining.WorkingMemory import WorkingMemory
from BackwardChaining.KnowledgeBase import KnowledgeBase
# from BackwardChaining.DepthFirstSearch import DepthFirstSearch


class InferenceEngine(object):
    """ Represents the application's Inference Engine: Match -> Select -> Act using Backward Chaining """

    def __init__(self):
        pass

    def depth_first_search(self, graph, start, goal):
        """ Performs Depth First Search, returns success for failure """
        # taken from http://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

        stack = [(start, [start])]

        print("Start stack: ", stack)

        while stack:
            (vertex, path) = stack.pop()

            for i in graph[vertex] - set(path):
                if i == goal:
                    yield path + [i]  # returns a generator
                    print(path + [i])
                    print("Goal found:", goal)
                else:
                    stack.append((i, path + [i]))

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
        """ Match a subgoal with antecedents from a rule, using Depth-First Search """
        pass

    def select(self):
        pass

    def act(self):
        pass
