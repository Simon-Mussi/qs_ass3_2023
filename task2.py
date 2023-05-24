from random import choices, randint


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

            assert is_balanced(test_case) == learned_model.execute_sequence(learned_model.initial_state, test_case)
    print('All random test cases conform to a model')


# input alphabet for both functions
input_alphabet = ['(', ')']

# TODO learn a model that passes the verify_correctness check for both functions

learned_model_funny_counter = None
verify_correctness(learned_model_funny_counter, 'funny_counter')

# TODO try to minimize a number of membership queries used for learning of is_balanced
learned_model_is_balanced = None
verify_correctness(learned_model_is_balanced, 'is_balanced')

