
from tracemalloc import start
from PySimpleAutomata import automata_IO, NFA, DFA
from graphviz import Digraph
from collections import deque
import graphviz


##Q1##

def generate_transition_diagram(states: set, alphabet: set, transitions: dict, start_state: str, accepting_states: set):
  dot = Digraph('example_graph', format='png')


  for i in states:
    if i in accepting_states:
      dot.node(str(i).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""),str(i).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""),shape='doublecircle')
    else:
      dot.node(str(i).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""),str(i).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""))

  ###Just add pointers
  for i in states:
    for x in alphabet:
      if type(transitions[i][x]) == frozenset:
        dot.edge(str(i).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""),str(transitions[i][x]).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""), label=x)
      else:
        for z in transitions[i][x]:
          dot.edge(str(i).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""), str(z).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""), label=x)


  dot.node('start', 'start', shape='point')
  dot.edge('start', str(start_state).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""), label="start")

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


##Q2##

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



  dfa_start_state = set()
  dfa_start_state.add(nfa_start_state)
  stack = [dfa_start_state]

  dfa_states = set()
  dfa_alphabet= set() 
  dfa_transitions = {} 
  dfa_accepting_states = set()


  #while there are unprocessed items
  while len(stack)>0:

    #pop the last item
    cur_state = stack.pop()

    cur_state = frozenset(cur_state)

    #if item has been processed, it will be in dfa_states
    if cur_state in dfa_states:
      continue

    #add to dfa states here to avoid double processing
    dfa_states.add(cur_state)

    for state in cur_state:
      if state in nfa_accepting_states:
        dfa_accepting_states.add(cur_state)
        break

    if cur_state not in dfa_transitions:
      dfa_transitions[cur_state]={}

    #for each character to transition on
    for char in nfa_alphabet:


      #create a set which will become the state the character transitions to
      curr_transitions = set()

      #add transitions from all states in the current dfa state
      for state in cur_state:
        for transition in nfa_transitions[state][char]:
          curr_transitions.add(transition)
      
      #add a transition to the dfa state(which is a set of states). dfa transitions should be of type dict[dict][set]
      fr_transitions = frozenset(curr_transitions)
      dfa_transitions[cur_state][char] = fr_transitions

      #if the new state has not been processed, add it to the stack 
      if curr_transitions not in dfa_states:
        stack.append(curr_transitions)

  

  return dfa_states, nfa_alphabet, dfa_transitions, str(frozenset(dfa_start_state)), dfa_accepting_states

    






dfa_states, dfa_alphabet, dfa_transitions, dfa_start_state, dfa_accepting_states = nfa_to_dfa(
    nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_accepting_states
)

print("\nDFA accepting states:")
for state in dfa_accepting_states:
  print(str(state).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""))



print("\nDFA states:")
for state in dfa_states:
  if state in dfa_accepting_states:
    print("**"+str(state).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""))
  elif str(state)==dfa_start_state:
    print("-->"+str(state).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""))
  else:
    print(str(state).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""))
print("\nDFA Transitions:")

for state in dfa_transitions:
  print(str(dfa_transitions[state]).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")","").replace("{","").replace("}","").replace("(","").replace(")",""))

generate_transition_diagram(dfa_states, dfa_alphabet, dfa_transitions, dfa_start_state, dfa_accepting_states)

  




    

    
            

    