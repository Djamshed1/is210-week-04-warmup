#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This a docstring for the 4th tasks"""

def too_many_kittens(kittens, litterboxes, catfood):
    """This ensures that there are enough litterbox for each kitten on not.

    Args:
        kittens(int): the number of kittens
        litterboxes(int): the number of available litterboxes
        catfood(bool): represents whether or not any catfood exists

    Returns:
        bool: 'If the number of litterboxs are greater than the number of kittens
        and catfood, return false. Otherwise, True

    Examples:
        >>> too_many_kittens(2, 3, 2)
        False

        >>> too_many_kittens(12, 12, False)
        True

        >>> too_many_kittens(13, 12, True)
        True

        >>> too_many_kittens(12, 13, True)
        False
    """
    return not (litterboxes >= kittens and catfood)
    
