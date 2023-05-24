import dill as pickle
from abc import ABC, abstractmethod


# interface that all loaded implementations implement
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


if __name__ == '__main__':

    # Load 3 implementations of the same interface
    black_box_models = []
    for model_pickle in ['vending_machine_dorian.pickle', 'vending_machine_edi.pickle',
                         'vending_machine_moritz.pickle', 'vending_machine_matthias.pickle']:

        with open(f'black_box_impl/{model_pickle}', 'rb') as handle:
            loaded_model = pickle.load(handle)
            black_box_models.append(loaded_model)

    # Example how to interact with the vending machine
    # get on of the vending machines
    vm = black_box_models[3]
    # reset it
    vm.reset()
    # perform an action
    print(vm.push_button('coke'))
    print(vm.add_coin(1))

    # TODOs
    # TODO 1. Learn models of Vending Machines
    # TODO 2. Write a function that performs leaning-based testing to find the differances between them (if any)
    # TODO 3. By performing an analysis of the learned models with function from TODO 2,
    #  figure out which model is correct, and what are the bugs in other models
    # TODO 4. Report the findings in the Report.md
