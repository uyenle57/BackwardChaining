# -*- coding: utf-8 -*-#


class Rule(object):
    """ Defines the antecedents and consequences of each rule in the Knowledge Base. """

    rule_number = ""
    antecedents = []
    consequences = ()

    def __init__(self, rule_number, antecedents, consequences):
        """ Initialise parameters. """

        self.rule_number = rule_number
        self.antecedents = antecedents
        self.consequences = consequences

    def get_antecedents(self):
        """ Returns the antecedents. """
        return self.antecedents

    def get_consequences(self):
        """ Returns the consequences. """
        return self.consequences

    def has_antecedents(self, antecedent):
        """ Checks if the given antecedent is in the antecedent list of the Knowledge Base. Returns True or False. """
        return antecedent in self.antecedents

    def has_consequences(self, consequent):
        """ Checks if the given consequent is in the consequences list of the Knowledge Base. Returns True or False. """
        return consequent == self.consequences

    def get_rule_number(self):
        """ Returns the number of the rule. """
        return self.rule_number

    def to_string(self):
        """ Returns the rule as a string in the IF (antecedent) THEN (consequent) format. """
        return "IF " + str(self.antecedents) + " \n\tTHEN " + str(self.consequences)
