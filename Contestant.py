
class Contestant:

    def __init__(self, first_name, last_name, email, registration_number):
        self.fname = first_name
        self.lname = last_name
        self.email = email
        self.registration_number = registration_number

    def notify(self, is_winner):
        print(is_winner + ' is the winner of the sweepstakes.')