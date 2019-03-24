#!/usr/bin/env python3


import random


def roll_dice(number, sides):
    """ Rolls the requested number of dice with given sides
        Note: statistically, 10d10 has a different distribution
        of results than 1d100, so the 'dice' should rolled
        independently

        Args: 'sides' - the number of sides to each die
              'number' - the number of dice to roll

        Returns: the roll result 
    """
    result = sum([random.randrange(1,sides+1) for i in range(number)])
    return result


def parse_dice(dice_desc):
    """ Takes a string that describes the dice, such as '4d10' and
        returns the number of dice and number of die sides

        Args: dice_desc - string describing the dice, ex "2d10" or '4D8'
                          a special case is allowed for whole numbers,
                          i.e., '12'

        Returns: a tuple (# of dice, # of die sides)

        Exceptions: ValueError when the input is ill-formatted
    """
    found_d = dice_desc.find('d') == True
    dice    = dice_desc.lower().split('d')

    try:
        if not found_d :
            number = int(dice[0])
            sides  = 1
        else :
            number = int(dice[0])
            sides  = int(dice[1])
        return number, sides
    except:
        raise ValueError("Dice descriptor must be in the format 'NdM' where 'N' is the number of dice" \
                          "and 'M' is the number of die sides!")


def dice_command(command):
    """ Parses and calculates the result for a full dice rolling command,
        such as 5d10+1d4+4

        Args: 'command' - a string with the requested dice rolling operation,
                          for example, 2d8+8

        Exceptions: ValueError when the input is ill-formatted
    """
    split_cmd = command.split('+')

    return sum([roll_dice(*parse_dice(cmd)) for cmd in split_cmd])