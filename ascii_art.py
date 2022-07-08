# Contains functions useful for making ASCII art

# Contains the digits 0-9 in ASCII art
ascii_art_digits = [
    [
        " _ ",
        "/ \\",
        "\\_/"
    ],
    [
        " .",
        "/|",
        " |"
    ],
    [
        "_ ",
        " )",
        "/_"
    ],
    [
        "_ ",
        "_)",
        "_)"
    ],
    [
        "   ",
        "|_|",
        "  |"
    ],
    [
        " _ ",
        "|_ ",
        " _)"
    ],
    [
        " _ ",
        "|_ ",
        "|_)"
    ],
    [
        "__",
        " /",
        "/ "
    ],
    [
        " _ ",
        "(_)",
        "(_)"
    ],
    [
        " _ ",
        "(_|",
        "  |"
    ]
]

# Converts the given integer into ASCII art
# Returns a list of three strings, each representing a line in the ASCII art
# If smush is true, the numbers will placed closer together
# Leading zeros will be added to meet minimum length
# The numbers are centered to the given width
# If stick_left is true, the integer will stick to the left when being centered
# Retuns an empty list if the arguments are not of expected type
def get_ascii_int(integer, length = 0, width = 0, smush = False, stick_left = True):
    if type(integer) is not int or type(length) is not int or type(width) is not int:
        return []
    digits = get_int_digits(integer, length)
    ascii_int = ['', '', '']
    for digit_pos in range(len(digits)):
        extra_space = ''
        # Current Digit
        ascii_digit = ascii_art_digits[digits[digit_pos]]
        # Previous Digit
        past_ascii_digit = ascii_art_digits[digits[digit_pos - 1]]
        if digit_pos != 0:
            if smush:
                for line in range(3):
                    c1 = past_ascii_digit[line][-1]
                    c2 = ascii_digit[line][0]
                    if c2 == '_':
                        # '|' touching '_' or '.' -> Ex: 93, 23
                        if c1 == '|' or c1 == '_' or c1 == '.':
                            extra_space = ' '
                            break
            else:
                extra_space = ' '
        for line in range(3):
            ascii_int[line] += extra_space + ascii_digit[line]
    ascii_int_width = len(ascii_int[0])
    if width > ascii_int_width:
        # ascii_int_lenght odd & width is even
        if not stick_left and ascii_int_width % 2 == 1 and width % 2 == 0:
            for line in range(3):
                ascii_int[line] = f" {ascii_int[line]}".center(width, ' ')
        # ascii_int_lenght even & width is odd
        elif stick_left and ascii_int_width % 2 == 0 and width % 2 == 1:
            for line in range(3):
                ascii_int[line] = f"{ascii_int[line]} ".center(width, ' ')
        else:
            for line in range(3):
                ascii_int[line] = ascii_int[line].center(width, ' ')
    return ascii_int

# Returns the digits of the given integer in a list
# Leading zeros will be added to meet minimum length
# Returns empty list if argument is not an int
def get_int_digits(integer, length = 0):
    if type(integer) is not int or type(length) is not int:
        return []
    str_int = str(integer)
    digits = [0] * (length - len(str_int))
    for str_digit in str_int:
        digits.append(int(str_digit))
    return digits
