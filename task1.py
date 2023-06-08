from aalpy.SULs import MealySUL
from aalpy.learning_algs import run_Lstar
from aalpy.oracles import RandomWordEqOracle
from random import seed, choices, randint
import dill as pickle
from abc import ABC, abstractmethod


class AbstractVendingMachine(ABC):

    @abstractmethod
    # user can add any coin (0.5, 1, 2)
    # you can experiment with more to better understand how automata learning works, but it is not necessary
    def add_coin(self, coin):
        pass

    @abstractmethod
    # possible orders are 'coke', 'peanuts', 'water'
    def push_button(self, order):
        pass

    @abstractmethod
    def reset(self):
        pass
    
class VendingMachineSUL(MealySUL):
    def __init__(self, vending_machine):
        super().__init__(None)  # Call MealySUL constructor without providing a Mealy Machine
        self.vending_machine = vending_machine
        self.reset()
        self.coin_count = 0

    def step(self, letter):
        if letter in {0.5, 1.0, 2.0}:
            self.coin_count += 1
            if self.coin_count > 5:
                self.coin_count = 5
            return self.vending_machine.add_coin(letter)
        else: 
            output = self.vending_machine.push_button(letter)
            self.coin_count = 0
            return output

    def get_input_alphabet(self):
        return [0.5, 1.0, 2.0, 'coke', 'peanuts', 'water']
    
    def pre(self):
        self.reset()

    def post(self):
        pass

    def reset(self):
        self.vending_machine.reset()

if __name__ == '__main__':

    # Load 3 implementations of the same interface
    black_box_models = []
    for model_pickle in ['vending_machine_dorian.pickle', 'vending_machine_edi.pickle',
                         'vending_machine_moritz.pickle', 'vending_machine_matthias.pickle']:
        with open(f'black_box_impl/{model_pickle}', 'rb') as handle:
            loaded_model = pickle.load(handle)
            black_box_models.append(loaded_model)
    seed(1)
    learned_models = []
    name = ['dorian', 'edi', 'moritz', 'matthias']
    cnt = 0
    # Wrap each vending machine model in a SUL and learn a Mealy machine model
    for vending_machine in black_box_models:
        sul = VendingMachineSUL(vending_machine)
        input_alphabet = sul.get_input_alphabet()
        eq_oracle = RandomWordEqOracle(input_alphabet, sul, num_walks=100, min_walk_len=3, max_walk_len=6)
        learned_model = run_Lstar(input_alphabet, sul, eq_oracle, automaton_type='mealy', print_level=3)
        learned_model.visualize(path='Learned_model_' + name[cnt] + '.pdf')
        learned_models.append(learned_model)
        cnt += 1

    # TODO 2. Write a function that performs learning-based testing to find the differences between them (if any)
    def compare_models(model1, model2, input_alphabet, num_tests=1000):
        differences = []
        for _ in range(num_tests):
            inputs = choices(input_alphabet, k=randint(8, 8))
            outputs1 = model1.execute_sequence(model1.initial_state, inputs)
            outputs2 = model2.execute_sequence(model2.initial_state, inputs)
            if outputs1 != outputs2:
                differences.append((inputs, outputs1, outputs2))
        return differences
    # Compare all pairs of models
    for i in range(len(learned_models)):
        for j in range(i + 1, len(learned_models)):
            differences = compare_models(learned_models[i], learned_models[j], input_alphabet)
            print(f"Differences between model {i} and model {j}:")
            for inputs, outputs1, outputs2 in differences:
                print(f"Inputs: ")
                print(f"{inputs}")
                print(f"Outputs for model {i}:")
                print(f"{outputs1}")
                print(f"Outputs for model {j}:")
                print(f"{outputs2}")

    # TODOs
    # TODO 1. Learn models of Vending Machines
    # TODO 2. Write a function that performs leaning-based testing to find the differances between them (if any)
    # TODO 3. By performing an analysis of the learned models with function from TODO 2,
    #  figure out which model is correct, and what are the bugs in other models
    # TODO 4. Report the findings in the Report.md
    # Define the possible actions
    
