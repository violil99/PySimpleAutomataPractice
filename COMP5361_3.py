
from tracemalloc import start
from PySimpleAutomata import automata_IO, NFA, DFA
from graphviz import Digraph
from collections import deque
import graphviz


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
    


    

    
            

    