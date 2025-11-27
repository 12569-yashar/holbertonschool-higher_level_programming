#!/usr/bin/python3
"""salam"""


def write_file(filename="", text=""):
    """salam"""
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
