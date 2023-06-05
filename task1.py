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
    
    # TODO 1
    def learn_model(vm, actions, num_trials=1000):
        """
        This function learns the behavior of a vending machine model by performing random sequences of actions
        and recording the results.
        """
        model_behavior = {}

        for _ in range(num_trials):
            sequence = random.choices(actions, k=random.randint(1, 10))  # Random sequence of actions
            sequence_str = ', '.join(map(str, sequence))
            vm.reset()
            output = []
            for action in sequence:
                if isinstance(action, float):  # If the action is adding a coin
                    output.append(vm.add_coin(action))
                else:  # If the action is pressing a button
                    output.append(vm.push_button(action))
            model_behavior[sequence_str] = output

        return model_behavior


    # TODO 2
    def learning_based_testing(vm1, vm2, actions, num_trials=1000):
        """
        This function performs learning-based testing on two vending machine models by executing the same sequence of
        actions on both and checking if their outputs differ.
        """
        differences = {}

        for _ in range(num_trials):
            sequence = random.choices(actions, k=random.randint(1, 10))  # Random sequence of actions
            sequence_str = ', '.join(map(str, sequence))
            vm1.reset()
            vm2.reset()
            output1 = []
            output2 = []
            for action in sequence:
                if isinstance(action, float):  # If the action is adding a coin
                    output1.append(vm1.add_coin(action))
                    output2.append(vm2.add_coin(action))
                else:  # If the action is pressing a button
                    output1.append(vm1.push_button(action))
                    output2.append(vm2.push_button(action))
            if output1 != output2:
                differences[sequence_str] = (output1, output2)

        return differences


        # Defining the possible actions
        actions = [0.5, 1, 2, 'coke', 'peanuts', 'water']

        # Learning the behavior of each vending machine
        vending_machine_behaviors = [learn_model(vm, actions) for vm in black_box_models]

        # Comparing the behavior of each pair of vending machines
        for i in range(len(black_box_models)):
            for j in range(i + 1, len(black_box_models)):
                print("---------------------------------------------------")
                print(f"Differences between model {i} and model {j}:")
                differences = learning_based_testing(black_box_models[i], black_box_models[j], actions)
                for sequence_str, outputs in differences.items():
                    print(f"For sequence: {sequence_str}")
                    print(f"Model {i} output:")
                    print(outputs)
