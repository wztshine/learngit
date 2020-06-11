from atm.core import log_in
from atm.core import transaction



def run():
    name = log_in.log_in()
    transaction.next_step(name)

