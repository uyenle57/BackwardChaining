# -*- coding: utf-8 -*-#

class KnowledgeBase():

    # facts = []
    rules = {}

    def __init__(self):

        # facts = [
        #     ('f','h'), ('a', 'c'), ('b', 'g'), ('n', 's'), ('e', 'm'),
        #     ('r', 't'), ('p', 'q'), ('d', 'j'), ('k', 'i'), ('u', 'v')
        # ]

        # Initialise rules and antecedents

        self.rules = {
            'Rule 1' : set([('f','h'), ('a', 'c')]),
            'Rule 2' : ('n', 's'),
            'Rule 3' : ('r', 't'),
            'Rule 4' : set([('d', 'j'), ('e', 'm'), ('k', 'i')]),
            'Rule 5' : ('p', 'q'),
            'Rule 6' : ('u', 'v')
        }

        sets = {('f','h'), ('a', 'c')}

        if sets == self.rules['Rule 1']:
            print('Matched!')


        # Define rules and facts
        # switch(rule):
        # default:
        # case rules[0]:
        #
        #     break
        # case rules[1]:
        #     break



    def getRules(self):
        return self.rules
