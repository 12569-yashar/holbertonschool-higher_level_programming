#!/usr/bin/python3
"""salam"""

import json


def load_from_json_file(filename):
    """salam """

    with open(filename, mode="r", encoding='utf-8') as my_file:
        return json.load(my_file)
