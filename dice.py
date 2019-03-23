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



