# -*- coding: utf-8 -*-#


class WorkingMemory(object):
    """ Represents the application's Working Memory. Contains a set of Facts. """

    facts = []

    def __init__(self, facts):
        """ Initialise initial Working Memory as a list of Facts """
        self.facts = facts

    def has_fact(self, fact):
        """ Check if the given fact is available in the Working Memory. Returns True or False. """
        return fact in self.facts

    def add_fact(self, fact):
        """ Add a fact to the Working Memory. """
        self.facts.append(fact)

    def get_facts(self):
        """ Returns all the facts in the Working Memory. """
        return self.facts
