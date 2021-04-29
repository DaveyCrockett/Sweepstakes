import random
from Contestant import Contestant


class Sweepstake:
    contestant_list = [{
        'first name': '',
        'last name': '',
        'email': '',
        'registration number': ''
    }]

    def __init__(self, name):
        self.name = name

    def register_contestant(self, contestant):
        self.contestant_list.append(contestant)

    def pick_winner(self):
        winner = random.choice(self.contestant_list)
        Contestant(winner)
        return winner

    def print_contestant_info(self, contestant):
        return print(contestant.first_name + ' ' + contestant.last_name + ', ' + contestant.email + ', ' + contestant.registration_number)

