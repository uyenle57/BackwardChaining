# -*- coding: utf-8 -*-#

class WorkingMemory():

    facts = []

    def __init__(self):

        # Initialise initial Working Memory as a list of Facts
        self.facts = [
            ('f','h'),
            ('d', 'j'),
            ('u', 'v'),
            ('r', 't')
        ]

    def getFacts(self):
        return self.facts

    # Update Working Memory using add and delete
    def addFact(self, newFact):
        return self.facts.append(newFact)

    def deleteFact(self, fact):
        return self.facts.remove(fact)
