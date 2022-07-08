# Contains functions used in the blind auction program
from io_handling import screen_states, error_states
from resources import blind_auction, bidder_num
from random import randint, choice

# TO DO -------------------------------------------------------------------
def add_bid():
    if generate_bidder_num():
        return -1 # Full Bid

    bidder_name = screen_states["get_name"]()
    blind_auction[bidder_num[0]] = {
        "bidder_name": bidder_name,
        "bid_amount": screen_states["get_bid"](bidder_name)
    }

# Calculates the winning bid for the blind auction
# If there's more than one top bid (equal), choose one randomly
def calculate_winning_bid():
    winning_bid = -1
    for bidder in blind_auction:
        current_bid = blind_auction[bidder]["bid_amount"]
        if current_bid == winning_bid:
            bidder_num.append(bidder)
        elif current_bid > winning_bid:
            winning_bid = current_bid
            bidder_num.clear()
            bidder_num.append(bidder)
    bidder_num[0] = choice(bidder_num)

# Generate a new, unique bidder number in the range of [0, 99999]
# Returns -1 if blind_auction is full
def generate_bidder_num():
    if len(blind_auction) == 100000: # 100000
        bidder_num[0] = "FULL"
        error_states["full_auction"]()
        return -1
    while True:
        bidder_num[0] = randint(0, 99999) # 0, 99999
        if bidder_num[0] not in blind_auction:
            break
