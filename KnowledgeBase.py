# -*- coding: utf-8 -*-#

from BackwardChaining.Rule import Rule


class KnowledgeBase(object):
    """" Responsible for managing the knowledge base. """

    rules = []

    def __init__(self):
        self.rules.append(Rule('R1', [('f', 'h'), ('a', 'c')], ('b', 'g')))
        self.rules.append(Rule('R2', [('n', 's')], ('e', 'm')))
        self.rules.append(Rule('R3', [('r', 't')], ('p', 'q')))
        self.rules.append(Rule('R4', [('d', 'j'), ('e', 'm'), ('k', 'i')], ('a', 'c')))
        self.rules.append(Rule('R5', [('p', 'q')], ('n', 's')))
        self.rules.append(Rule('R6', [('u', 'v')], ('k', 'i')))

    def get_rules(self):
        """ Returns the rules. """
        return self.rules

    def get_hypotheses(self):
        """ Returns all the hypotheses starting from the given goal. """

        hypotheses = []

        # Adds the elements in rule to the end of hypotheses list
        for rule in self.rules:
            hypotheses.extend(rule.get_antecedents())
        return hypotheses

    def get_rule_with_antecedents(self, antecedent):
        """ Returns the corresponding rule for the given antecedent. """

        for rule in self.rules:
            if rule.has_antecedents(antecedent):
                return rule
        return None

    def get_rule_with_consequences(self, consequences):
        """ Returns the corresponding rule for the given consequences. """

        for rule in self.rules:
            if rule.has_consequences(consequences):
                return rule
        return None
