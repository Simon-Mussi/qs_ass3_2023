from random import choices, randint
from aalpy.SULs import MealySUL
from aalpy.learning_algs import run_Lstar
from aalpy.utils import generate_random_deterministic_automata
from aalpy.oracles import KWayTransitionCoverageEqOracle
from aalpy.oracles import WMethodEqOracle
from aalpy.oracles import RandomWordEqOracle, RandomWMethodEqOracle
from aalpy.base import SUL
from aalpy.automata import MealyMachine
import re
from random import seed


seed(1)

def is_balanced(x):
    len_x = len(x)
    if len_x % 2 != 0 or len_x == 0:
        return False
    middle = (len_x - 1) // 2
    for i in range(middle + 1):
        if x[i] != '(' or x[middle + 1 + i] != ')':
            return False
    return True


def funny_counter(x, n=3):
    return len(x) % n


def verify_correctness(learned_model, function_under_test):
    assert function_under_test in {'funny_counter', 'is_balanced'}

    for _ in range(100000):
        if function_under_test == 'funny_counter':
            test_case = choices(['(', ')'], k=randint(10, 20))
            sul_output = funny_counter(test_case)
            learned_model_output = learned_model.execute_sequence(learned_model.initial_state, test_case)[-1]
        else:
            test_passing = randint(0, 1)
            x = randint(1, 10)
            test_case = list('(' * x + ')' * x)
            if not test_passing:
                mut = randint(1, len(test_case) - 1)
                test_case[mut] = '(' if test_case[mut] == ')' else ')'

            sul_output = is_balanced(test_case)
            learned_model_output = learned_model.execute_sequence(learned_model.initial_state, test_case)[-1]

        if sul_output != learned_model_output:
            print(f'Failing test-case : {test_case}')
            print(f'SUL output        : {sul_output}')
            print(f'Learned Model     : {learned_model_output}')

            assert(False)
            #assert is_balanced(test_case) == learned_model.execute_sequence(learned_model.initial_state, test_case)
    print('All random test cases conform to a model')


# input alphabet for both functions
input_alphabet = ['(', ')']

# TODO learn a model that passes the verify_correctness check for both functions

class RegexSUL(SUL):
    def __init__(self, input: str):
        super().__init__()
        self.input = input
        self.list = []

    def pre(self):
        self.list = []
        pass

    def post(self):

        pass

    def step(self, letter):
        if(letter is not None):
            self.list.append(letter)
        return is_balanced(self.list)

model0 = RegexSUL(input_alphabet)

#eq_oracle = KWayTransitionCoverageEqOracle(input_alphabet, model, k = 11, optimize='queries')
eq_oracle = WMethodEqOracle(input_alphabet, model0, 22)

learned_model_is_balanced = run_Lstar(input_alphabet, model0, eq_oracle, automaton_type='dfa', print_level=3)
verify_correctness(learned_model_is_balanced, 'is_balanced')



class RegexSUL(SUL):
    def __init__(self, input: str):
        super().__init__()
        self.input = input
        self.list = []

    def pre(self):
        self.list = []
        pass

    def post(self):

        pass

    def step(self, letter):
        if(letter is not None):
            self.list.append(letter)
        return funny_counter(self.list)

model1 = RegexSUL(input_alphabet)

eq_oracle = KWayTransitionCoverageEqOracle(input_alphabet, model1, 6)

learned_model_funny_counter = run_Lstar(input_alphabet, model1, eq_oracle, automaton_type='dfa', print_level=3)
verify_correctness(learned_model_funny_counter, 'funny_counter')

# TODO try to minimize a number of membership queries used for learning of is_balanced

eq_oracle = KWayTransitionCoverageEqOracle(input_alphabet, model0, k=9, num_generate_paths=1000,
                                            max_number_of_steps=9, method="prefix",
                                            max_path_len=9, optimize="queries")

learned_model_is_balanced = run_Lstar(input_alphabet, model0, eq_oracle, automaton_type='dfa', print_level=2)
verify_correctness(learned_model_is_balanced, 'is_balanced')
