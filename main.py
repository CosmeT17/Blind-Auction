# Blind Auction

# TO Do: Better Title -----------------
from resources import titles
from time import sleep
from random import choice

print(choice(titles), end='', flush=True)
sleep(2)
# -------------------------------------

from bid_functions import add_bid, calculate_winning_bid
from io_handling import bool_input, print_results

get_bidders = True
while get_bidders:
    # Add new bid to blind_auction dictionary
    if add_bid():
        break  # Full Auction

    # Run loop again if there are more bidders
    get_bidders = bool_input("\nAny more bidders (Y/N)?")

# Print the results of the acution
calculate_winning_bid()
print_results()
