# -*- coding: utf-8 -*-#


class WorkingMemory(object):
    """ This represents the application's working memory """

    facts = []

    def __init__(self, facts):
        """ Initialise initial Working Memory as a list of Facts """
        self.facts = facts

    def has_fact(self, fact):
        """ Return True in the working memory has the fact else False."""
        return fact in self.facts

    def add_fact(self, fact):
        """ Add a fact to the Working Memory. """
        self.facts.append(fact)

    def get_facts(self):
        """ Returns the facts of the Working Memory. """
        return self.facts
