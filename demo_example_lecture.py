from random import seed, choices, randint
from aalpy.SULs import MealySUL
from aalpy.learning_algs import run_Lstar
from aalpy.oracles import RandomWordEqOracle
from aalpy.utils import generate_random_deterministic_automata

seed(1)
# Randomly generate some model that we want to learn
random_model = generate_random_deterministic_automata('mealy', num_states=3, input_alphabet_size=2,
                                                      output_alphabet_size=2)
# Get its input alphabet
input_al = random_model.get_input_alphabet()
# Wrap it in SUL interface
sul = MealySUL(random_model)
# define eq. oracle
eq_oracle = RandomWordEqOracle(input_al, sul, num_walks=100, min_walk_len=3, max_walk_len=6)
# run the learning algorithm
learned_model = run_Lstar(input_al, sul, eq_oracle, automaton_type='mealy', print_level=3,)
# learned_model.visualize()
print(learned_model)

print('Printing prefixes of states')
for state in learned_model.states:
    print(state.prefix)

characterization_set = learned_model.compute_characterization_set()
print('Char. set:', characterization_set)

print('Get outputs string from input string')
inputs = choices(input_al, k=5)
print('Inputs', inputs)
outputs = learned_model.execute_sequence(learned_model.initial_state, inputs)
print('Outputs', outputs)

print('Testing for equivalence')
for _ in range(1000):
    random_inputs = choices(input_al, k=randint(5, 50))
    assert learned_model.execute_sequence(learned_model.initial_state, random_inputs) == random_model.execute_sequence(random_model.initial_state, random_inputs)
