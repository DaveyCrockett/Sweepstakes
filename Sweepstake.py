from Contestant import Contestant


class Sweepstake:

    def __init__(self, name):
        name =
        self.contestant_list = [{
            'first name': Contestant().first_name,
            'last name': Contestant().last_name,
            'email': Contestant().email,
            'registration number': Contestant().registration_number
        }]

    def register_contestant(self, contestant):
        self.contestant_list.append(contestant)

    def pick_winner(self):
        winner = Contestant() # needs parameters
        return winner

    def print_contestant_info(self, contestant):
        print(contestant)

