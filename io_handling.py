# Contains functions used for printing the logo, results, and errors
from resources import logo, bidder_num, blind_auction
from ascii_art import get_ascii_int
from readchar import readkey
from re import sub, match
from replit import clear

# Cosntants
NAME_PROMPT = "Bidder Name: "
BID_PROMPT = "Bid Amount: $"

# Returns true if the key entered is 'y'/'Y', false if 'n'/'N', keeps asking otherwise
# Prints the prompt
def bool_input(prompt):
    print(prompt, end = '', flush = True)
    while True:
        answer = readkey().lower()
        if answer == 'y':
            print()
            return True
        elif answer == 'n':
            print()
            return False

# Clears the screen, prints the logo w/ bidder num
# def print_logo():
#     clear()
#     print(logo(get_ascii_int(bidder_num[0], 5, 15, True)))
#     # print(f"Bidder #: {bidder_num[0]}\n")

# TO DO --------------------------------------------------------
def print_results():
    # print_logo()
    clear()
    print(logo(get_ascii_int(bidder_num[0], 5, 15, True)))

    print(f"Winning Bidder: {blind_auction[bidder_num[0]]['bidder_name']}")
    print(f"Winning Bid: ${blind_auction[bidder_num[0]]['bid_amount']}")
    
    # FOR TESTING PURPOSES --------------------------------------
    print()
    print(blind_auction)
    # FOR TESTING PURPOSES --------------------------------------

# Clears the screen, prints the logo, prints the text + result (formated), returns result 
def clear_print(txt, result):
    # print_logo()
    clear()
    print(logo(get_ascii_int(bidder_num[0], 5, 15, True)))

    if type(result) is float:
            print(f"{txt}{'{:.2f}'.format(result)}")
    else:
        print(f"{txt}{result}")
    return result

# Clears the screen, prints the logo, prints the prompt, returns the input
def clear_input(prompt):
    # print_logo()
    clear()
    print(logo(get_ascii_int(bidder_num[0], 5, 15, True)))

    # Change input method here -> sometimes normal, sometimes senitive
    return input(prompt)

# Contains functions corrsponding to different error states
error_states = {
    "invalid_name": lambda: clear_input("Please enter a valid name: "),
    "invalid_bid": lambda name: clear_input(f"{NAME_PROMPT}{name}\nPlease enter a non-negative real number: $"),
    "full_auction": lambda: clear_input("Full auction, press any key to continue...")
}

# Contains functions corresponding to different program states
screen_states = {
    "get_name": lambda: clear_print(NAME_PROMPT, check_name(clear_input(NAME_PROMPT))),
    "get_bid": lambda name: clear_print(f"{NAME_PROMPT}{name}\n{BID_PROMPT}", check_bid(clear_input(f"{NAME_PROMPT}{name}\n{BID_PROMPT}"), name))
}

# Returns name properly formatted if it is a valid, otherwise keep asking for a name
def check_name(name):
    while True:
        name = format_name(name)
        if sub("\.|'| ", '', name).isalpha():
            break
        name = error_states["invalid_name"]()
    return name

# Returns bid amount properly formatted if it is a valid, otherwise keep asking for a bid amount
def check_bid(bid, name):
    while True:
        try: 
            bid = float(bid)
        except ValueError:
            bid = error_states["invalid_bid"](name)
            continue
        if bid <= 0:
            bid = error_states["invalid_bid"](name)
            continue
        return bid

# Returns name properly formatted
def format_name(name):
    name = name.strip()
    if name == '':
        return ''
    name = sub(" +", ' ', name).lower()
    name = name[0].upper() + name[1:]
    f_name = ""
    for char in range(len(name)):
        if bool(match(" .", name[char - 1: char + 1])):
            f_name += name[char].upper()
            continue
        f_name += name[char]
    return f_name
