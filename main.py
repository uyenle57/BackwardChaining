# -*- coding: utf-8 -*-#import textwrapfrom KnowledgeBase import *from WorkingMemory import *from InferenceEngine import *def main():    print(textwrap.dedent("""    ================================================================                      ARTIFICIAL INTELLIGENCE            Coursework 2: Backward Chaining Rule Based System                                Uyen Le                        tle004@gold.ac.uk    ================================================================    \n"""))    print("Knowlegde Base:\n")    # KNOWLEDGE BASE: contains Rules and Facts    knowledgeBase = KnowledgeBase()    rules = knowledgeBase.get_rules()    for i in range(0, len(rules)):        print("Rule " + str(i + 1) + "\t" + rules[i].to_string() + "\n")    # Define the goal    goal = ['b', 'g']    print('\nGoal: ', goal)    workingMemory = WorkingMemory()    print("\nWorking Memory:\n")    print(workingMemory.get_facts())main()