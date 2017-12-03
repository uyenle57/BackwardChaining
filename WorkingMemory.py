# -*- coding: utf-8 -*-#


class WorkingMemory(object):
    """ This represents the application's working memory """

    facts = []

    def __init__(self):
        """ Initialise initial Working Memory as a list of Facts """

        self.facts = [
            ('f', 'h'),
            ('d', 'j'),
            ('u', 'v'),
            ('r', 't')
        ]

    def has_fact(self, fact):
        """ Return True in the working memory has the fact else False."""
        return fact in self.facts

    def get_facts(self):
        return self.facts
