# -*- coding: utf-8 -*-
"""COMP5361_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QVZ2rPxKOp-lmvIFheV1MwkK_5j6RuvS

# **Important Requirements**
"""

from tracemalloc import start
from PySimpleAutomata import automata_IO, NFA, DFA
from graphviz import Digraph
from collections import deque
import graphviz

"""# Program 1: Generating Transition Diagram using PySimpleAutomata

https://pysimpleautomata.readthedocs.io/en/latest/


The generate_transition_diagram function takes the following parameters:

* states: Set of states in the automaton.
* alphabet: Set of symbols in the alphabet.
* transitions: Dictionary representing transitions between states for each symbol.
* start_state: The initial state.
* accepting_states: Set of accepting states.

It uses the graphviz library to create a DOT graph, where nodes represent states, and edges represent transitions. Accepting states are represented with a double circle.

## Format of input for generate_transition_diagram function
"""


"""## Format of output for generate_transition_diagram function

![transition_diagram.png](data:image/png;base64,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)

# Using Digraph
"""


# Output file: example_graph.png






def generate_transition_diagram(states: set, alphabet: set, transitions: dict, start_state: str, accepting_states: set):
  dot = Digraph('example_graph', format='png')

  for i in states:
    if i in accepting_states:
      dot.node(i,i,shape='doublecircle')
    else:
      dot.node(i,i)

  ###Just add pointers
  for i in states:
    for x in alphabet:
      for z in transitions[i][x]:
        dot.edge(i, z, label=x)


  dot.node('start', 'start', shape='point')
  dot.edge('start', start_state, label="start")

  dot.render('example_graph', format='png', cleanup=True)


    
# Example of Input:
states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transitions = {
    'q0': {'0': {'q0', 'q1'}, '1': {'q0'}},
    'q1': {'0': set(), '1': {'q2'}},
    'q2': {'0': set(), '1': set()}
}
start_state = 'q0'
accepting_states = {'q2'}


generate_transition_diagram(states, alphabet, transitions, start_state, accepting_states)

  





'''
  #Use a deque to create a stack, initialized with the epsilon closure of the NFA start state, represented as a frozenset.
  dfa_states = set()
  dfa_transitions = set()
  dfa_accepting_states = set()

  start = set()
  start.add(start_state)
  stack = start

  processed= set()



while len(stack)>0:
  current_nfa_state = stack.pop()
  current_dfa_state = frozenset(current_nfa_state)
  if(current_dfa_state in processed):
    continue
  processed.add(current_dfa_state)

  for i in current_dfa_state:
    if i in accepting_states:
      dfa_accepting_states.add(current_dfa_state)

  for i in alphabet:
    next_nfa_states = set()
    for x in current_nfa_state:
      if x in transitions[i]:
        next_nfa_states.add(transitions[i][x])
    #Compute the epsilon closure of next_nfa_states to handle epsilon transitions.
    next_dfa_state = frozenset(next_nfa_states)
    if next_dfa_state not in dfa_transitions:
      stack.append(next_dfa_state)
      dfa_transitions[current_dfa_state]=next_dfa_state


  dot.render('example_graph', format='png', cleanup=True)
  return dfa_states, alphabet, dfa_transitions,dfa_start_state,dfa_accepting_states


'''  

'''
def intermediate(states: set, alphabet: set, transitions: dict, start_state: str, accepting_states: set, processed,dot):

    currNode = start_state

    if currNode in processed:# or len(currNode)==0:
      return
    
    if currNode in accepting_states:
      dot.node(currNode,currNode,shape='doublecircle')
    else:
      dot.node(currNode,currNode)
    
    processed.append(currNode)


    for i in alphabet:
      for x in transitions[currNode]:
        if len(transitions[currNode][i][x])==0:
          continue
        nextNode = intermediate(states, alphabet, transitions, transitions[currNode][i][x], accepting_states, processed)
        dot.edge(currNode, nextNode, label=i)
    
'''


states = {'q0', 'q1', 'q2'}
alphabet = {'0', '1'}
transitions = {
    'q0': {'0': {'q0', 'q1'}, '1': {'q0'}},
    'q1': {'0': set(), '1': {'q2'}},
    'q2': {'0': set(), '1': set()}
}
start_state = 'q0'
accepting_states = {'q2'}
generate_transition_diagram(states,alphabet,transitions,start_state,accepting_states)
    


    

    
            

    




"""## Question One:

## Algorithm Steps:
1. Initialize DFA States and Transition Table:
* Initialize an empty set dfa_states to store states of the DFA.
* Initialize an empty dictionary dfa_transitions to store transitions between DFA states.
* Use a deque to create a stack, initialized with the epsilon closure of the NFA start state, represented as a frozenset.
* Initialize an empty set processed_states to keep track of processed states to avoid redundancy.
2. Explore NFA States to Generate DFA States:
* While the stack is not empty:
  * Pop a set of NFA states current_nfa_states from the stack.
  * Convert the set to a frozenset, representing a state in the DFA (current_dfa_state).
  * If the DFA state is already processed, skip to the next iteration.
  * Mark the DFA state as processed.
  * Add the DFA state to the set of DFA states (dfa_states).
  * Check if any NFA state in current_nfa_states is an accepting state, and if so, add the DFA state to the set of accepting states (dfa_accepting_states).
3. Explore Transitions for Each Symbol:
* For each symbol in the alphabet:
  * Create an empty set next_nfa_states to store the next set of NFA states.
  * For each NFA state in current_nfa_states:
      * If there is a transition for the symbol in the NFA state, add the target states to next_nfa_states.
  * Compute the epsilon closure of next_nfa_states to handle epsilon transitions.
  * Convert the set to a frozenset (next_dfa_state).
  * If next_dfa_state is not in the DFA transitions, push it onto the stack for further exploration.
  * Update the DFA transition table with the transition from current_dfa_state to next_dfa_state on the current symbol.
4. Return DFA Information:
 * Return the set of DFA states (dfa_states), alphabet (alphabet), transition table (dfa_transitions), start state (dfa_start_state), and accepting states (dfa_accepting_states).

## Key Concepts:
* The algorithm uses a stack to explore the possible states in the DFA.
* Each state in the DFA represents a set of NFA states.
* Epsilon closures are used to handle epsilon transitions in the NFA.
* The algorithm ensures that each DFA state is processed only once to avoid redundancy.

# Question Two:

## Algorithm Explanation:
### Initialization:

* dfa_states: Set of states in the DFA.
* dfa_transitions: Dictionary representing transitions between states in the DFA.
* dfa_start_state: The start state of the DFA.
* dfa_accepting_states: Set of accepting states in the DFA.

### Conversion Process:

* The algorithm uses a stack to keep track of sets of NFA states that need to be processed.
* It starts with the set containing the start state of the NFA (nfa_start_state).

### Main Loop:

* While the stack is not empty, the algorithm processes sets of NFA states to determine transitions and states in the corresponding DFA.
* For each symbol in the alphabet:
  * Determine the set of NFA states that can be reached from the current set of NFA states using the symbol.
  * Convert this set of NFA states to a frozenset and add it to the DFA states.
  * If the new state is not in the stack, add it to the stack for further processing.
  * Update the DFA transitions with the transition from the current DFA state with the given symbol to the new DFA state.

### Accepting States:

* If any state in the current set of NFA states is an accepting state, add the corresponding DFA state to the set of accepting states.

### Repeat:

* Continue processing until the stack is empty.

### Result:

* The resulting dfa_states, dfa_transitions, dfa_start_state, and dfa_accepting_states represent the equivalent DFA.

### Input Parameters:
* nfa_states: Set of states in the NFA.
* alphabet: Set of symbols in the alphabet.
* nfa_transitions: Dictionary representing transitions between states in the NFA.
* nfa_start_state: The start state of the NFA.
* nfa_accepting_states: Set of accepting states in the NFA.

## Question two Input:
"""

# Example Input
nfa_states = {'q0', 'q1', 'q2'}
nfa_alphabet = {'0', '1'}
nfa_transitions = {
    'q0': {'0': {'q0', 'q1'}, '1': {'q0'}},
    'q1': {'0': set(), '1': {'q2'}},
    'q2': {'0': set(), '1': set()}
}
nfa_start_state = 'q0'
nfa_accepting_states = {'q2'}

def nfa_to_dfa(nfa_states, nfa_alphabet, nfa_transitions,nfa_start_state, nfa_accepting_states):
  stack = 1


#dfa_states, dfa_alphabet, dfa_transitions, dfa_start_state, #dfa_accepting_states = nfa_to_dfa(
 #   nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_accepting_states
#)

#print("DFA States:", dfa_states)
#print("DFA Transitions:", dfa_transitions)

'''
call the function:
dfa_states, dfa_alphabet, dfa_transitions, dfa_start_state, dfa_accepting_states = nfa_to_dfa(
    nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_accepting_states
)

print("DFA States:", dfa_states)
print("DFA Transitions:", dfa_transitions)
'''

"""# **Example 1: frozenset**"""

# Creating a frozenset
nfa_states = {'q0', 'q1', 'q2'}
nfa_states_frozen = frozenset(nfa_states)

# Frozensets are immutable and can be used as keys in dictionaries
state_transitions = {nfa_states_frozen: {'0': {'q0', 'q1'}, '1': {'q0'}}}

print("NFA States Frozen:", nfa_states_frozen)
print("State Transitions:", state_transitions)

# Creating frozensets
set1 = frozenset({1, 2, 3})
set2 = frozenset({3, 4, 5})

# Frozensets are hashable and can be used as keys in dictionaries
set_dict = {set1: 'Set 1', set2: 'Set 2'}

print("Set 1:", set1)
print("Set 2:", set2)
print("Set Dictionary:", set_dict)

"""# **Example 2: deque**"""

from collections import deque

# Creating a deque
stack = deque([1, 2, 3])

# Adding elements to the deque
stack.append(4)
stack.append(5)

# Removing elements from the deque
popped_element = stack.pop()

print("Stack:", stack)
print("Popped Element:", popped_element)

# Creating a deque
my_deque = deque([1, 2, 3, 4, 5])

# Appending elements
my_deque.append(6)

# Popping elements
popped_element = my_deque.pop()

# Appending elements to the left
my_deque.appendleft(0)

# Popping elements from the left
popped_element_left = my_deque.popleft()

print("Deque:", my_deque)
print("Popped Element:", popped_element)
print("Deque after appendleft and popleft:", my_deque)

"""# **Example 3: .update() with Sets**"""

# Using .update() to update a set with another set
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)

print("Updated Set:", set1)