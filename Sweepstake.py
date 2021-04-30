import random
from Contestant import Contestant


class Sweepstake:

    def __init__(self, name):
        self.name = name
        self.contestant_list = []
    def register_contestant(self, contestant):
        self.contestant_list.append(contestant)


    def pick_winner(self):
        winner = random.choice(self.contestant_list)
        win_info = Contestant(winner)
        return win_info

    def print_contestant_info(self, contestant):
        return print(contestant.fname, contestant.lname, contestant.email, contestant.reg)

