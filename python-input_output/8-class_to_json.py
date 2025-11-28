#!/usr/bin/python3
"""salam"""


def class_to_json(obj):
    """salam"""

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
