#!/usr/bin/python3
"""salam"""


def write_file(filename="", text=""):
    """salam"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
