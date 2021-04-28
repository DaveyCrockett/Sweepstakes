from Contestant import Contestant
from user_interface import user_interface

class Sweepstake:
    contesant = [{

    }]

    def __init__(self, name):
        name = user_interface().get_string_input()

    def register_contestant(self, contesant):
        pass

    def pick_winner(self):
        winner = Contestant() # needs parameters
        return winner

    def print_contestant_info(self, contestant):
        print(contestant)
