# -*- coding: utf-8 -*-#


class Rule(object):
    """ Defines the antecedents and consequences of each rule in the Knowledge Base """

    antecedents = []
    consequences = ()

    def __init__(self, antecedents, consequences):
        self.antecedents = antecedents
        self.consequences = consequences

    def get_antecedents(self):
        return self.antecedents

    def get_consequent(self):
        return self.consequences

    def to_string(self):
        return "IF " + str(self.antecedents) + " \n\tTHEN " + str(self.consequences)
