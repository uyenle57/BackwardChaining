# -*- coding: utf-8 -*-#

import textwrap
from KnowledgeBase import *
from WorkingMemory import *
from InferenceEngine import *


def main():

    print(textwrap.dedent("""
    ================================================================
                      ARTIFICIAL INTELLIGENCE
            Coursework 2: Backward Chaining Rule Based System
    
                            Uyen Le
                        tle004@gold.ac.uk
    ================================================================
    """))


    # Depth-First Search
    def depthFirstSearch():
        pass

    # KNOWLEDGE BASE
    # contains Rules and Facts
    knowledgeBase = KnowledgeBase()
    knowledgeBase.echo()

    # WORKING MEMORY
    # contains Facts
    workingMemory = WorkingMemory()
    workingMemory.echo()

    # INFERENCE ENGINE
    # Match -> Select -> Act
    inferenceEngine = InferenceEngine()
    inferenceEngine.echo()
    
main()


