import dill as pickle
from aalpy.base import SUL
from aalpy.oracles import RandomWalkEqOracle

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
from aalpy.SULs.PyMethodSUL import FunctionDecorator



# =============
# DO NOT REMOVE
from collections import defaultdict, Counter
import random

random.random()
placeholder = defaultdict(Counter)
# ==============

from Message import Message

seed(1)
class MessageBoardInterface:
    def __init__(self):
        pass

    def publish_message(self, client: str, message: str) -> str:
        pass

    def retrieve_messages(self, target_client: str) -> list[Message]:
        pass

    def search_messages(self, search_string: str) -> list[Message]:
        pass

    def report(self, reporter: str, target_client: str) -> str:
        pass

    def remove_report(self, reporter: str, target_client: str) -> str:
        pass

    def like_message(self, initiator: str, target_client: str, target_message: str) -> str:
        pass

    def dislike_message(self, initiator: str, target_client: str, target_message: str) -> str:
        pass

    def remove_like(self, initiator: str, target_client: str, target_message: str, ) -> str:
        pass

    def remove_dislike(self, initiator: str, target_client: str, target_message: str, ) -> str:
        pass

    def edit_message(self, initiator: str, target_client: str, message_to_edit: str, new_message: str) -> str:
        pass

    def delete_message(self, initiator: str, target_client: str, message_to_delete: str) -> str:
        pass

    def react(self, initiator: str, target_client: str, message_to_react_to: str, reaction: str) -> str:
        pass

    def reset(self):
        pass


possible_reactions = {'smiley', 'laughing', 'crying', 'frown', 'horror', 'surprise', 'skeptical', 'cool'}

with open(f'black_box_impl/message_board.pickle', 'rb') as handle:
    correct_message_bord = pickle.load(handle)

with open(f'black_box_impl/message_board_0.pickle', 'rb') as handle:
    message_board_0 = pickle.load(handle)

with open(f'black_box_impl/message_board_1.pickle', 'rb') as handle:
    message_board_1 = pickle.load(handle)

with open(f'black_box_impl/message_board_2.pickle', 'rb') as handle:
    message_board_2 = pickle.load(handle)

# TODO 1. For all 3 variations of the message board, find shortest test-cases described
#  in the assignment sheet using learning-based testing

class PyClassSUL(SUL):
    """
    System under learning for inferring python classes.
    """
    def __init__(self, python_class):
        """
        Args:

            python_class: class to be learned
        """
        super().__init__()
        self._class = python_class
        self.sul: object = None

    def pre(self):
        """
        Do the reset by initializing the class again or call reset method of the class
        """
        self.sul = self._class()

    def post(self):
        pass

    def step(self, letter):
        """
        Executes the function(with arguments) found in letter against the SUL

        Args:

            letter: single input of type FunctionDecorator

        Returns:

            output of the function

        """
        if letter.args:
            return getattr(self.sul, letter.function.__name__, letter)(*letter.args)
        return getattr(self.sul, letter.function.__name__, letter)()
    

model1 = PyClassSUL(correct_message_bord)
model2 = PyClassSUL(message_board_1)

func1 = FunctionDecorator(MessageBoardInterface.publish_message(), {'client1', 'testmessage'})
func2 = FunctionDecorator(MessageBoardInterface.like_message(), list('client2', 'client1', 'testmessage'))
func3 = FunctionDecorator(MessageBoardInterface.dislike_message(), list('client2', 'client1', 'testmessage'))

input_alphabet = [func1, func2, func3]

eq_oracle = RandomWalkEqOracle(input_alphabet, model1,num_steps = 5000,reset_after_cex=True)

learned_model = run_Lstar(input_alphabet, model1, eq_oracle, automaton_type='mealy')

# at this point, model is learned
# to do the Learning-based testing, we simply use the model as a hypothesis for other systems/implementations
# in cases of non-conformance, counterexample will be returned

# note that the SUL passed to the eq_oracle is not the one that we used for learning
eq_oracle = RandomWalkEqOracle(input_alphabet, model2, num_steps=5000,reset_after_cex=True)

counter_example = eq_oracle.find_cex(learned_model)
if counter_example:
  print('Counterexample found', counter_example)
else:
  print('No counterexample found')


# TODO 2. Describe the found bugs, and present the shortest test-case in the report
