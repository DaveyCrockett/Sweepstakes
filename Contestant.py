from user_interface import user_interface


class Contestant:

    def __init__(self):
        self.first_name = user_interface().get_string_input('What is the contestants first name?')
        self.last_name = user_interface().get_string_input('What is the contestants last name?')
        self.email = user_interface().get_string_input('What is the contestants email?')
        self.registration_number = int(user_interface().get_string_input('What is the contestants registration number?'))

    def notify(self, is_winner):
        pass