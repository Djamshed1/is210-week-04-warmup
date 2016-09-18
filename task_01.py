#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""

def know_what_i_mean(wink, numwink=2):
    """This code returns a string with some winks and nudges.

    Args:
        wink(int):'An argument which gets repeated 2 times because numwink
        string.'
        numwink(str): The number of times a wink will be repeated. Default:2
        
    Returns:
        str:'The arguments concatenated with commas and winks and nudges gets
        multiplied by numwink value.'
        
    Examples:
        >>>know_what_i_mean(wink)
        'Know what I mean? winkwink, nudge nudge'
        
        >>> know_what_i_mean('wink', 3)
        'Know what I mean? winkwinkwink, nudge nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {0}, {1}'.format(winks, nudges)
    return retstr
