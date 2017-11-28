# -*- coding: utf-8 -*-#

class Rule():

    antecedents = []
    consequence = ()

    def __init__(self, antecedents, consequence):
        self.antecedents = antecedents
        self.consequence = consequence

    def get_antecedents(self):
        return self.antecedents

    def get_consequence(self):
        return self.consequence

    def to_string(self):
        return "IF " + str(self.antecedents) + " \n\tTHEN " + str(self.consequence)
