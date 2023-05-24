import dill as pickle

# =============
# DO NOT REMOVE
from collections import defaultdict, Counter
import random

random.random()
placeholder = defaultdict(Counter)
# ==============

from Message import Message


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
# TODO 2. Describe the found bugs, and present the shortest test-case in the report
