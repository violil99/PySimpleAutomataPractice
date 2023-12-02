#Lilith Richter-Stephenson 40288772


from tracemalloc import start
from PySimpleAutomata import automata_IO, NFA, DFA
from graphviz import Digraph
from collections import deque
import graphviz


##Q1##

#takes sets of states, alphabet, and accepting state. As well as a nested dictionary of transitions, and a stre representing the starting state.
#outputs a representation of the states in graph form. 
'''Transitions to set states (i.e. state = ('q1','q2') not states = ('q1), ('q2')) MUST be in frozenset form'''
def generate_transition_diagram(states: set, alphabet: set, transitions: dict, start_state: str, accepting_states: set):

  #setting up the digraph to output into example_graph.png
  dot = Digraph('example_graph', format='png', graph_attr={'size': '20,20', 'dpi':'300'})


  #Creates nodes for every state, with a double circle around accepting states
  #Removes unnecessary characters "frozenset","(",")","{","}"
  for i in states:
    if i in accepting_states:
      dot.node(str(i).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""),str(i).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""),shape='doublecircle')
    else:
      dot.node(str(i).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""),str(i).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""))

  #Adds pointers between nodes based on transitions table
  for i in states:
    for x in alphabet:

      #If transition leads to a frozenset, the transitions leads to a single state consisting of a set
      #And there should be a single pointer to that state
      if type(transitions[i][x]) == frozenset:
        dot.edge(str(i).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""),str(transitions[i][x]).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""), label=x)

      #Otherwise, there should be a pointer from state i on letter x to every 
      # state in that category of the transition dictionary
      else:
        for z in transitions[i][x]:
          dot.edge(str(i).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""), str(z).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""), label=x)


  #creating a start pointer
  dot.node('start', 'start', shape='point')
  dot.edge('start', str(start_state).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""), label="start")

  #rendering the graph
  dot.render('example_graph', format='png', cleanup=True)


    
#Input
states = {'q1', 'q2', 'q3', 'q4','q5','q6','q7','q8','q9','q10','D','F'}
alphabet = {'a', 'b'}
transitions = {

    ##q1 has seen 0 as, q6 has see 5
    'q1': {'a': {'q2'}, 'b': {'D'}},
    'q2': {'a': {'q3'}, 'b': {'q7'}},
    'q3': {'a': {'q4'}, 'b': {'q9'}},
    'q4': {'a': {'q5'}, 'b': {'q10'}},
    'q5': {'a': {'q6'}, 'b': {'q10'}},
    'q6': {'a': {'q6'}, 'b': {'F'}},


    #q7 has seen 1 b
    'q7': {'a': {'D'}, 'b': {'q8'}},
    'q8': {'a': {'D'}, 'b': {'q9'}},
    'q9': {'a': {'D'}, 'b': {'q10'}},
    'q10': {'a': {'D'}, 'b': {'F'}},

    'F': {'a': {'D'}, 'b': {'F'}},
    'D': {'a': {'D'}, 'b': {'D'}},
}
start_state = 'q1'
accepting_states = {'F'}

#generating the transition diagram
generate_transition_diagram(states, alphabet, transitions, start_state, accepting_states)


##Q2##

#input data(same as above)

nfa_states = {'q0', 'q1', 'q2'}
nfa_alphabet = {'0', '1'}
nfa_transitions = {
    'q0': {'0': {'q0', 'q1'}, '1': {'q0'}},
    'q1': {'0': set(), '1': {'q2'}},
    'q2': {'0': set(), '1': set()}
}
nfa_start_state = 'q0'
nfa_accepting_states = {'q2'}

#takes in an nfa with the same type of input as the above function, and converts it into a dfa.
#Every "set state" returned is in the form of a frozenset. communicating that that set should be
#considered a single state
def nfa_to_dfa(nfa_states, nfa_alphabet, nfa_transitions,nfa_start_state, nfa_accepting_states):



  #putting the start state into set form so that it can be read 
  #in the same way as the other states
  dfa_start_state = set()
  dfa_start_state.add(nfa_start_state)

  #adding the start state to the stack to be processed
  stack = deque([dfa_start_state])

  #setting dfa information to be returned
  #nfa and dfa alphabet 
  dfa_states = set()
  dfa_transitions = {} 
  dfa_accepting_states = set()


  #while there are unprocessed items
  while len(stack)>0:

    #pop the last item
    cur_state = stack.pop()

    #make current state a frozenset
    cur_state = frozenset(cur_state)

    #if item has been processed, it will be in dfa_states
    if cur_state in dfa_states:
      continue

    #add to dfa states here to avoid double processing
    dfa_states.add(cur_state)

    # for each nfa state in the current state (which is a set of states)
    # check if the nfa state is an accepting state, and if so, add the entire 
    # current set of states to dfa accepting states. dfa accepting states will 
    # include every state which includes an nfa accepting state
    for state in cur_state:
      if state in nfa_accepting_states and cur_state not in dfa_accepting_states:
        dfa_accepting_states.add(cur_state)
        break

    #Starts a new dictionary for the current state if not already processed
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
      
      #add a transition to the dfa state(which is a set of states). 
      #dfa transitions should be of type dict[dict][set]
      fr_transitions = frozenset(curr_transitions)
      dfa_transitions[cur_state][char] = fr_transitions

      #if the new state has not been processed, add it to the stack 
      if curr_transitions not in dfa_states:
        stack.append(curr_transitions)

  
  #once the stack is empty (all accessible states have been processed), return all information on the dfa
  return dfa_states, nfa_alphabet, dfa_transitions, str(frozenset(dfa_start_state)), dfa_accepting_states



#Make NFA into DFA, storing all DFA variables
dfa_states, dfa_alphabet, dfa_transitions, dfa_start_state, dfa_accepting_states = nfa_to_dfa(
    nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_accepting_states
)

#Print accepting states
print("\nDFA accepting states:")
for state in dfa_accepting_states:
  print(str(state).replace("frozenset","").replace("{","").replace("}","").replace("(","").replace(")",""))


#Print all dfa states with --> pointing to start state and **before accepting states
print("\nDFA states:")
for state in dfa_states:
  if state in dfa_accepting_states:
    print("**"+str(state).replace("frozenset","").replace("{","").replace("}",""))
  elif str(state)==dfa_start_state:
    print("-->"+str(state).replace("frozenset","").replace("{","").replace("}",""))
  else:
    print(str(state).replace("frozenset","").replace("{","").replace("}",""))

#Print all dfa transitions with --> pointing from the starting state to the information about its 
print("\nDFA Transitions:")
for state in dfa_transitions:
  print(str(state).replace("frozenset","").replace("{","").replace("}",""),"-->",str(dfa_transitions[state]).replace("frozenset","").replace("{","").replace("}",""))


'''Use this to generate the transition diagram for the dfa version'''
#generate_transition_diagram(dfa_states, dfa_alphabet, dfa_transitions, dfa_start_state, dfa_accepting_states)

  




    

    
            

    