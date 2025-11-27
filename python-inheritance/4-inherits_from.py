#!/usr/bin/python3
"""this is document"""


def inherits_from(obj, a_class):
    """this is documnet"""
    a = isinstance(obj, a_class)
    b = type(obj) is not a_class
    return a and b
