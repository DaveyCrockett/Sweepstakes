from MarketingFirm import MarketingFirm
from MarketingFirmCreator import MarketingFirmCreator


def run_simulation():
    manager_choice = MarketingFirmCreator().choose_manager_type()
    MarketingFirm(manager_choice)


if __name__ == '__main__':
    run_simulation()