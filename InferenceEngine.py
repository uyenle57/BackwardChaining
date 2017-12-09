# -*- coding: utf-8 -*-#

from BackwardChaining.WorkingMemory import WorkingMemory
import sys


class InferenceEngine(object):
    """ Represents the application's Inference Engine: Match -> Select -> Act using Backward Chaining """

    def __init__(self, working_memory, knowledge_base):

        # Knowledge Base
        self.knowledge_base = knowledge_base

        # Facts from the Working Memory
        self.working_memory = working_memory

        self.current_working_memory = WorkingMemory([])

        # Explored set for goal test
        self.explored = []

        self.start_goal = None

    def backward_chaining(self, goal):
        """ Performs Backward Chaining by recursively matching the consequences with each hypothesis in the working memory. """

        # Make sure goal exists
        if goal:
            # Make a copy of the goal as 'start_goal', to be used for the act() function
            self.start_goal = goal
            self.match_goal(goal) # Start matching the given goal
        else:
            print("ERROR: Goal not found.")
            sys.exit(1)

    def match_goal(self, goal):
        """ Match a goal/hypothesis with a consequent using Depth-First Search. """

        print("\n------------------------")
        print("Hypothesis:", goal)
        print("------------------------")

        # Select the matching rule
        selected_rules = self.select(goal)
        print("Select rule:", selected_rules)

        # For each hypothesis
        for sub_goal in selected_rules:
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
                # Try to match with that antecedent as a new hypothesis
                self.match_sub_goal(sub_goal)

    def match_sub_goal(self, sub_goal):
        """ Match a sub-goal with antecedents from a rule """

        self.match_goal(sub_goal)

    def select(self, goal):
        """ Select the matching antecedents for a given goal. """

        for rule in self.knowledge_base.get_rules():
            if rule.has_consequences(goal):
                return rule.get_antecedents()

    def act(self, goal):
        """ Fires a chain of rules that satisfy the goal. """

        # List to store the fired rules
        rules_fired = []

        # Find the corresponding rule for the given goal
        rule = self.knowledge_base.get_rule_with_antecedents(goal)

        # Generate chain of rules for the goal
        while rule is not None:
            rules_fired.append(rule)

            # Get the corresponding rule of the given consequences
            rule = self.knowledge_base.get_rule_with_antecedents(rule.get_consequences())

            # The given goal can be both an antecedent and consequent
            # Get the corresponding rule for 'goal_rule' if it's an antecedent
            if rule is not None:
                goal_rule = self.knowledge_base.get_rule_with_antecedents(self.start_goal)

                # Also, get the corresponding rule for 'goal_rule' if it's a consequent
                if goal_rule is None:
                    goal_rule = self.knowledge_base.get_rule_with_consequences(self.start_goal)

                # Compare the rule number of 'rule' is same as 'goal_rule'
                # if same then add the rule to rules_fired list
                if goal_rule.get_rule_number() == rule.get_rule_number():
                    rules_fired.append(rule)
                    rule = None

        return rules_fired

    def print_fired_rules(self, rules_fired):
        """ Print the chain of fired rules. """

        string = ""

        for index in range(0, len(rules_fired)):
            string = string + rules_fired[index].get_rule_number()
            if index + 1 is not len(rules_fired):
                string = string + " -> "

        return string
