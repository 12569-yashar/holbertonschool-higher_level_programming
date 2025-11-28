#!/usr/bin/python3
"""salaammm"""


def class_to_json(obj):
    a={}
    if hasattr (obj, __dict__):
        a = obj.__dict__.copy()
    return a
