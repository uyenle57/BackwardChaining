# -*- coding: utf-8 -*-#

class Rule():

    antecedents = []
    consequence = ()

    def __init__(self, antecedents, consequent):
        self.antecedents = antecedents
        self.consequent = consequent

    def get_antecedents(self):
        return self.antecedents

    def get_consequent(self):
        return self.consequent

    def to_string(self):
        return "IF " + str(self.antecedents) + " \n\tTHEN " + str(self.consequent)
