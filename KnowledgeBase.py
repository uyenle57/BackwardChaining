# -*- coding: utf-8 -*-#

from Rule import Rule

class KnowledgeBase(object):
    ''' Responsible for managing the knowledge base. The rule base. '''

    rules = []

    def __init__(self):
        self.rules.append(Rule([('f', 'h'), ('a', 'c')], ('b', 'g')))
        self.rules.append(Rule([('n', 's')], ('e', 'm')))
        self.rules.append(Rule([('r', 't')], ('p', 'q')))
        self.rules.append(Rule([('d', 'j'), ('e', 'm'), ('k', 'i')], ('a', 'c')))
        self.rules.append(Rule([('p', 'q')], ('n', 's')))
        self.rules.append(Rule([('u', 'v')], ('k', 'i')))

    def get_rules(self):
        return self.rules
