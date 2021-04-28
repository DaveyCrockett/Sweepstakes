from Contestant import Contestant
import random


class Sweepstake:

    def __init__(self):
        self.name = ''
        self.contestant_list = [{
            'first name': Contestant().first_name,
            'last name': Contestant().last_name,
            'email': Contestant().email,
            'registration number': Contestant().registration_number
        }]

    def register_contestant(self, contestant):
        self.contestant_list.append(contestant)

    def pick_winner(self):
        winner = random.choice(self.contestant_list)
        return winner

    def print_contestant_info(self, contestant):
        print(contestant.first_name + ' ' + contestant.last_name + ', ' + contestant.email + ', ' + contestant.registration_number)

