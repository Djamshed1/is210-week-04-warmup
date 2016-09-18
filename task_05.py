#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This docstring is for task 05."""

def defaults(my_required, my_optional = True):
    """This function compares two boolean values.

    Args:
        my_optional(mixed): This fuction has a default value of True
        my_required(mixed): This is a required param and has no default value

    Returns:
        bool: Returns a logical value comparison of my_optional and my_required.
        
    Examples:
        >>> defaults(True, True)
        True

        >>> defaults(False, True)
        False

        >>> defaults('apple', 'grapes')
        False
    """

    return my_optional is my_required
