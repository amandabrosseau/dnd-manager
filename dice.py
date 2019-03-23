#!/usr/bin/env python3


import random


def roll_dice(sides, number):
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

        Returns: a tuple (# of dice, # of die sides)
    """
    dice = dice_desc.lower().split('d')

    try:
        if len(dice) != 2 : raise ValueError
        number = int(dice[0])
        sides  = int(dice[1])
        return number, sides
    except:
        raise ValueError("Dice descriptor must be in the format 'NdM' where 'N' is the number of dice \
                          and 'M' is the number of die sides!")