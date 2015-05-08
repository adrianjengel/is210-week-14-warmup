#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""WK14 warmup task 02 - using comprehensions."""


from data import FRUIT


def get_cost_per_item(shoplist):
    """A function to calculate the cost per item on a shopping list.

    Args:
        shoplist(dict): A list of items.

    Example:
        >>> shoplist = {
        'Apple': 4,
        'Beet': 2,
        'Black Plum': 10,
        'Grenade Pluot': 5}
        >>> get_cost_per_item(shoplist)
        {'Grenade Pluot': 9.95, 'Black Plum': 29.900000000000002}

    """
    return {key: FRUIT[key] * shoplist[key] for key in
            shoplist.iterkeys() if key in FRUIT}


def get_total_cost(shoplist):
    """A function to calculate the total cost of all items together.

    Args:
        shoplist(dict): A list of items.

    Example:
        >>> shoplist = {
        'Apple': 4,
        'Beet': 2,
        'Black Plum': 10,
        'Grenade Pluot': 5}
        >>> get_total_cost(shoplist)
        39.85

    """
    return sum(val for val in get_cost_per_item(shoplist).itervalues())
