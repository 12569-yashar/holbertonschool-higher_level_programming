#!/usr/bin/python3
"""salam"""


def inherits_from(obj, a_class):
    """salam"""
    if type(obj) == a_class:
        return False
    return issubclass(type(obj), a_class)
