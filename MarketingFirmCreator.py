from MarketingFirm import MarketingFirm
from SweepstakesQueueManager import SweepstakesQueueManager
from SweepstakesStackManager import SweepStakesStackManager
from user_interface import user_interface


class MarketingFirmCreator:

    def choose_manager_type(self):
        choice = user_interface().get_string_input('Do you want to use a stack or queue manager?')
        if choice == 'stack':
            MarketingFirm(SweepStakesStackManager())
        elif choice == 'queue':
            MarketingFirm(SweepstakesQueueManager())
