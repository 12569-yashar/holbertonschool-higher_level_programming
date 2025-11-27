#!/usr/bin/python3
"""salam"""

import json


def load_from_json_file(filename):
    """salam"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

