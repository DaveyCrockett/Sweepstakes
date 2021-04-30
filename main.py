from MarketingFirmCreator import MarketingFirmCreator
from Sweepstake import Sweepstake
from user_interface import user_interface
from Contestant import Contestant
from MarketingFirm import MarketingFirm


def run_simulation():
    manager_choice = MarketingFirmCreator().choose_manager_type()
    start_sweep = MarketingFirm(manager_choice).create_sweepstakes()
    i = 0
    while i < 3:
        contestant_first_name = user_interface().get_string_input('What is the contestants first name?')
        contestant_last_name = user_interface().get_string_input('What is the contestants last name?')
        contestant_email = user_interface().get_string_input('What is the contestants email?')
        contestant_reg = user_interface().get_string_input('What is the contestants registration number?')
        new_contestant = Contestant(contestant_first_name, contestant_last_name, contestant_email, contestant_reg)
        Sweepstake(start_sweep).register_contestant(new_contestant)
        Sweepstake(start_sweep).print_contestant_info(new_contestant)
        i += 1
    winner = Sweepstake(start_sweep).pick_winner()
    contestants = Sweepstake(start_sweep).contestant_list
    for single_contestant in contestants:
        Contestant.notify(winner)







if __name__ == '__main__':
    run_simulation()