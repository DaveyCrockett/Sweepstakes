from Sweepstake import Sweepstake

class MarketingFirm:

    def __init__(self, manager):
        self.manager = manager

    def create_sweepstakes(self):
        sweepstakes = Sweepstake('New Sweep')
        new_sweepstakes = self.manager.insert_sweepstakes(sweepstakes)
        return new_sweepstakes







