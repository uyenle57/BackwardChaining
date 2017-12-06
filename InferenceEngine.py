# -*- coding: utf-8 -*-#

from BackwardChaining.KnowledgeBase import KnowledgeBase
from BackwardChaining.WorkingMemory import WorkingMemory


class InferenceEngine(object):
    """ Represents the application's Inference Engine: Match -> Select -> Act using Backward Chaining """

    # Knowledge Base
    knowledge_base = KnowledgeBase()
    kBase = knowledge_base.get_rules()

    # Facts from the Working Memory
    working_memory = WorkingMemory()
    work_mem_facts = working_memory.get_facts()

    current_working_memory = []

    antecedents = []
    consequences = []
    goals = []

    graph = {}

    def __init__(self):

        # Get consequences
        for i in range(0, (len(self.kBase)-6)):
            self.consequences.append(self.kBase[i].get_consequences())

        # print("Consequences:", str(self.consequences))

        # Get antecedents
        for i in range(0, (len(self.kBase)-6)):
            self.antecedents.append(self.kBase[i].get_antecedents())

        # print("Antecedents:", str(self.antecedents))

        # Initialise temp Knowledge Base
        self.graph = {
            ('b', 'g'): set([('f', 'h'), ('a', 'c')]),
            ('f', 'h'): set(),
            ('a', 'c'): set([('d', 'j'), ('e', 'm'), ('k', 'i')]),
            ('d', 'j'): set(),
            ('k', 'i'): set([('u', 'v')]),
            ('u', 'v'): set(),
            ('e', 'm'): set([('n', 's')]),
            ('n', 's'): set([('p', 'q')]),
            ('p', 'q'): set([('r', 't')])
        }

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

    def backward_chaining(self, goal):
        """ Performs Backward Chaining by recursively matching the consequences with each hypothesis in the working memory. """

        # Make sure goal exists
        if goal:
            new_goals = self.match_goal(goal) # Start by matching with the given goal

            for goal in new_goals:
                if goal in set(self.work_mem_facts):
                    print(goal, "---> available in Working Memory.\n")
                    self.current_working_memory.append(goal)
                    print("Current Working Memory: ", self.current_working_memory)
                else:
                    self.match_sub_goal(goal)

    def match_goal(self, goal):
        """ Match a goal/hypothesis with a consequent, using Depth-First Search. Returns matched sub-goal."""
        print("\n------------------------")
        print("Hypothesis:", goal)
        print("------------------------")

        # TO DO use DFS

        for consequent in self.consequences:
            if consequent == goal:
                sub_goal = self.graph[consequent]
        print("Sub-goals:", sub_goal)
        return sub_goal

    def match_sub_goal(self, sub_goal):
        """ Match a sub-goal with antecedents from a rule, using Depth-First Search """

        # TO DO use DFS

        return self.match_goal(sub_goal)

    def select(self):
        pass

    def act(self):
        pass
