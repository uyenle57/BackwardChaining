# -*- coding: utf-8 -*-#

from BackwardChaining.WorkingMemory import WorkingMemory
import sys


class InferenceEngine(object):
    """ Represents the application's Inference Engine: Match -> Select -> Act using Backward Chaining. """

    def __init__(self, working_memory, knowledge_base):

        # Knowledge Base
        self.knowledge_base = knowledge_base

        # The global Working Memory
        self.working_memory = working_memory

        # A local Working Memory of the Inference Engine
        # used to keep track of which elements are available in the global Working Memory
        self.current_working_memory = WorkingMemory([])

        # Explored set for goal test
        self.explored = []

        self.start_goal = None

    def backward_chaining(self, goal):
        """ Performs Backward Chaining by recursively matching the consequences with each hypothesis in the Working Memory. """

        # Make sure goal exists
        if goal:
            # Make a copy of the goal as 'start_goal', used in act()
            self.start_goal = goal
            # Start matching the given goal
            self.match_goal(goal)
        else:
            print("ERROR: Goal not found.")
            sys.exit(1)

    def match_goal(self, goal):
        """ Match a goal/hypothesis with a consequent using Depth-First Search. """

        print("\n------------------------")
        print("Hypothesis:", goal)
        print("------------------------")

        # First, select the antecedent that matches with the goal
        selected_antecedents = self.select(goal)
        print("Select rule:", selected_antecedents)

        # For each hypothesis
        for sub_goal in selected_antecedents:
            # Add explored hypothesis to the explored set
            self.explored.append(sub_goal)

            # For each rule whose consequent matches this hypothesis
            # Try to match each of the rule antecedent with the facts from the Working Memory
            if self.working_memory.has_fact(sub_goal):

                # If matched, add the antecedent to the current working memory
                print(sub_goal, "---> available in Working Memory.")
                self.current_working_memory.add_fact(sub_goal)

                # Fire on the chain of rules once it's proven
                rules_fired = self.act(sub_goal)
                print("\nFires: ", self.print_fired_rules(rules_fired))
                print("Current working memory", self.current_working_memory.get_facts())

            else:
                # If antecedent does not match with the facts from the Working Memory
                # Add that antecedent as a new hypothesis, and try to match it
                self.match_sub_goal(sub_goal)

    def match_sub_goal(self, sub_goal):
        """ Match a sub-goal with antecedents from a rule. """
        self.match_goal(sub_goal)

    def select(self, goal):
        """ Select the matching antecedents for a given goal. """

        for rule in self.knowledge_base.get_rules():
            if rule.has_consequences(goal):
                return rule.get_antecedents()

    def act(self, goal):
        """ Fires a chain of rules that satisfy the goal. """

        rules_fired = []

        # Find the corresponding rule number for the given antecedent (which in this case is the goal)
        rule = self.knowledge_base.get_rule_with_antecedents(goal)

        # Generate chain of rules for the goal
        while rule is not None:

            # First, add that rule to the empty rules_fired list
            rules_fired.append(rule)

            # The hypothesis can be both an antecedent and consequent
            # So here we get the corresponding rule of the antecedent by passing in its consequences
            rule = self.knowledge_base.get_rule_with_antecedents(rule.get_consequences())

            # We do the same for the copy of the goal: 'start_goal'
            # Get the corresponding rule of 'start_goal' if it's an antecedent
            if rule is not None:
                goal_rule = self.knowledge_base.get_rule_with_antecedents(self.start_goal)

                # If it's not, then get the corresponding rule of 'start_goal' if it's a consequent
                if goal_rule is None:
                    goal_rule = self.knowledge_base.get_rule_with_consequences(self.start_goal)

                # Compare if the rule number of 'rule' is same as 'goal_rule'
                # if same then add that rule to rules_fired list
                if goal_rule.get_rule_number() == rule.get_rule_number():
                    rules_fired.append(rule)
                    rule = None

        return rules_fired

    def print_fired_rules(self, rules_fired):
        """ Returns the chain of fired rules as a string with '->' as the separator. """

        string = ""

        # Get the corresponding rule number for each rule in the 'rules_fired' list
        for rule_num in range(0, len(rules_fired)):
            # add the rule number to the empty string
            string = string + rules_fired[rule_num].get_rule_number()

            # Check if the current rule is in the 'rules_fired' list
            if rule_num + 1 is not len(rules_fired): # (rule_num+1 because the first rule is Rule 1, not Rule 0)
                # if so, add the '->' separator between each rule number
                string = string + " -> "

        return string
